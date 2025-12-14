import sys
import time
import math
import argparse

import cv2
import numpy as np
import mediapipe as mp
import pyautogui

from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QVBoxLayout,
    QWidget,
    QMainWindow,
)

# 1. Disable FailSafe so moving to corner doesn't crash app
pyautogui.FAILSAFE = False

class VideoThread(QThread):
    frame_ready = pyqtSignal(np.ndarray)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.running = False
        self.cap = None
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7,
        )
        # Store coordinates
        self.last_index = None      # Tip (8)
        self.last_thumb = None      # Tip (4)
        self.last_pinky = None      # Tip (20) - FOR RIGHT CLICK
        self.last_angle = -90       # Rotation

        # --- TUNING ---
        self.pinch_threshold = 0.05 
        
    def calculate_angle(self, p1, p2):
        """Calculates angle of the hand in degrees."""
        x1, y1 = p1.x, p1.y
        x2, y2 = p2.x, p2.y
        radians = math.atan2(y2 - y1, x2 - x1)
        return math.degrees(radians)

    def run(self):
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.running = True
        
        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                time.sleep(0.1)
                continue

            # Mirror effect
            frame = cv2.flip(frame, 1)
            h, w, _ = frame.shape
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            results = self.hands.process(rgb)

            self.last_index = None
            self.last_thumb = None
            self.last_pinky = None

            if results.multi_hand_landmarks:
                hand = results.multi_hand_landmarks[0]
                
                # --- Get Landmarks ---
                lm_index = hand.landmark[8]        # Index Tip
                lm_thumb = hand.landmark[4]        # Thumb Tip
                lm_pinky = hand.landmark[20]       # Pinky Tip (Landmark 20)
                
                # For Rotation: 0 = Wrist, 9 = Middle MCP (Knuckle)
                lm_wrist = hand.landmark[0]
                lm_middle_mcp = hand.landmark[9]

                # Store for UI thread
                self.last_index = (lm_index.x, lm_index.y)
                self.last_thumb = (lm_thumb.x, lm_thumb.y)
                self.last_pinky = (lm_pinky.x, lm_pinky.y)
                
                # Calculate Hand Rotation Angle
                self.last_angle = self.calculate_angle(lm_wrist, lm_middle_mcp)

                # --- Draw Visualization ---
                ix, iy = int(lm_index.x * w), int(lm_index.y * h)
                tx, ty = int(lm_thumb.x * w), int(lm_thumb.y * h)
                px, py = int(lm_pinky.x * w), int(lm_pinky.y * h) # Pinky coords
                
                wx, wy = int(lm_wrist.x * w), int(lm_wrist.y * h)
                mx, my = int(lm_middle_mcp.x * w), int(lm_middle_mcp.y * h)
                
                # Draw "Active Zone"
                margin = 80
                cv2.rectangle(frame, (margin, margin), (w - margin, h - margin), (0, 255, 255), 1)
                
                # Draw fingers
                cv2.circle(frame, (ix, iy), 8, (0, 255, 0), -1)      # Index (Green)
                cv2.circle(frame, (tx, ty), 8, (0, 0, 255), -1)      # Thumb (Red)
                cv2.circle(frame, (px, py), 8, (255, 0, 255), -1)    # Pinky (Purple)
                
                # Draw Lines for Pinches
                cv2.line(frame, (ix, iy), (tx, ty), (255, 255, 255), 1) # Left Click Line
                cv2.line(frame, (px, py), (tx, ty), (255, 0, 255), 1)   # Right Click Line

            self.frame_ready.emit(frame)

        if self.cap:
            self.cap.release()

    def stop(self):
        self.running = False
        self.wait()


class MainWindow(QMainWindow):
    def __init__(self, *, dry_run: bool = False, pinch_threshold: float = None,
                 smoothing: float = None, margin: float = None,
                 scroll_speed: int = None, angle_deadzone_min: float = None,
                 angle_deadzone_max: float = None):
        super().__init__()
        self.setWindowTitle("AI Mouse: Pinky Right Click")
        self.setGeometry(100, 100, 700, 500)
        self.setStyleSheet("background-color: #222; color: white;")

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        self.status_label = QLabel("Index Pinch: Left | Pinky Pinch: Right")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #00ffcc;")
        layout.addWidget(self.status_label)

        self.video_label = QLabel(alignment=Qt.AlignCenter)
        self.video_label.setStyleSheet("border: 2px solid #444; border-radius: 8px;")
        layout.addWidget(self.video_label)

        # Threading
        self.thread = VideoThread()
        # allow CLI override of pinch threshold
        if pinch_threshold is not None:
            self.thread.pinch_threshold = pinch_threshold
        self.thread.frame_ready.connect(self.update_image)
        self.thread.start()

        # --- MOUSE STATE ---
        self.screen_w, self.screen_h = pyautogui.size()
        
        # State Flags
        self.is_dragging = False
        self.is_right_clicked = False # Prevents spamming right click
        
        self.curr_x, self.curr_y = 0, 0
        self.prev_x, self.prev_y = 0, 0

        # defaults (can be overridden by CLI args)
        self.smoothing = 0.15 if smoothing is None else smoothing
        self.margin = 0.15 if margin is None else margin

        # Scroll settings
        self.scroll_speed = 40 if scroll_speed is None else scroll_speed
        self.angle_deadzone_min = -110 if angle_deadzone_min is None else angle_deadzone_min
        self.angle_deadzone_max = -70 if angle_deadzone_max is None else angle_deadzone_max

        # dry-run disables pyautogui side-effects
        self.dry_run = bool(dry_run)

        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.move_mouse)
        self.timer.start(8) 

    def update_image(self, cv_img):
        rgb = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb.shape
        qt_img = QImage(rgb.data, w, h, ch * w, QImage.Format_RGB888)
        self.video_label.setPixmap(QPixmap.fromImage(qt_img).scaled(640, 480, Qt.KeepAspectRatio))

    def move_mouse(self):
        idx = self.thread.last_index
        th = self.thread.last_thumb
        pinky = self.thread.last_pinky
        angle = self.thread.last_angle
        
        if idx is None or th is None:
            return

        # ============================
        # 1. SCROLL MODE
        # ============================
        is_scrolling = False
        
        if angle > self.angle_deadzone_max:
            if not self.dry_run:
                pyautogui.scroll(-self.scroll_speed) # Scroll Down
            self.status_label.setText("SCROLLING DOWN")
            self.status_label.setStyleSheet("color: orange; font-size: 22px; font-weight: bold;")
            is_scrolling = True
            
        elif angle < self.angle_deadzone_min:
            pyautogui.scroll(self.scroll_speed)  # Scroll Up
            self.status_label.setText("SCROLLING UP")
            self.status_label.setStyleSheet("color: orange; font-size: 22px; font-weight: bold;")
            is_scrolling = True

        # ============================
        # 2. CURSOR MOVE MODE
        # ============================
        if not is_scrolling:
            x_norm, y_norm = idx
            
            target_x = np.interp(x_norm, (self.margin, 1 - self.margin), (0, self.screen_w))
            target_y = np.interp(y_norm, (self.margin, 1 - self.margin), (0, self.screen_h))

            target_x = max(0, min(self.screen_w, target_x))
            target_y = max(0, min(self.screen_h, target_y))

            distance = math.hypot(target_x - self.prev_x, target_y - self.prev_y)
            if distance < 3.0:
                target_x = self.prev_x
                target_y = self.prev_y
            
            self.curr_x = self.prev_x + (target_x - self.prev_x) * self.smoothing
            self.curr_y = self.prev_y + (target_y - self.prev_y) * self.smoothing
            
            try:
                if not self.dry_run:
                    pyautogui.moveTo(self.curr_x, self.curr_y, _pause=False)
            except Exception:
                pass
                
            self.prev_x, self.prev_y = self.curr_x, self.curr_y

            # ============================
            # 3. CLICK LOGIC
            # ============================
            
            # --- A. LEFT CLICK / DRAG (Index + Thumb) ---
            left_pinch_dist = math.hypot(idx[0] - th[0], idx[1] - th[1])
            
            if left_pinch_dist < self.thread.pinch_threshold:
                if not self.is_dragging:
                    if not self.dry_run:
                        pyautogui.mouseDown()
                    self.is_dragging = True
                    self.status_label.setText("LEFT DRAG / CLICK")
                    self.status_label.setStyleSheet("color: red; font-size: 22px; font-weight: bold;")
            else:
                if self.is_dragging:
                    if not self.dry_run:
                        pyautogui.mouseUp()
                    self.is_dragging = False

            # --- B. RIGHT CLICK (Pinky + Thumb) ---
            if pinky:
                right_pinch_dist = math.hypot(pinky[0] - th[0], pinky[1] - th[1])
                
                if right_pinch_dist < self.thread.pinch_threshold:
                    if not self.is_right_clicked:
                        if not self.dry_run:
                            pyautogui.rightClick()
                        self.is_right_clicked = True
                        self.status_label.setText("RIGHT CLICK")
                        self.status_label.setStyleSheet("color: violet; font-size: 22px; font-weight: bold;")
                else:
                    self.is_right_clicked = False

            # Reset Label if nothing is happening
            if not self.is_dragging and not self.is_right_clicked:
                self.status_label.setText(f"Active (Angle: {int(angle)}°)")
                self.status_label.setStyleSheet("color: #00ffcc; font-size: 18px; font-weight: bold;")

    def closeEvent(self, event):
        self.thread.stop()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())