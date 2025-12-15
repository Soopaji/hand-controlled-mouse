<div align="center">

# 🖱️ AI Virtual Mouse

![Python](https://img.shields.io/badge/Python-3670A0?style=plastic&logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=plastic&logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-00BFFF?style=plastic&logo=google&logoColor=white)
![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-FF5733?style=plastic&logo=pypi&logoColor=white)

<br />

<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjEx.../giphy.gif" alt="Virtual Mouse Demo" width="700"/>

<br />

**Control your computer mouse with just your hand gestures.**
<br />
<a href="#-installation">Installation</a> • 
<a href="#-how-it-works">How It Works</a> • 
<a href="#-features">Features</a>

</div>

---

## 📝 About The Project

This project utilizes **Computer Vision** to create a virtual mouse system. By tracking hand landmarks via a webcam, it maps the movement of your index finger to the screen's cursor and recognizes specific gestures (like pinching or finger folding) to perform clicks and scrolls.

No extra hardware is needed—just a webcam and some Python magic.

## ✨ Features

* **Cursor Movement:** Smooth tracking of the index finger to move the mouse.
* **Left Click:** Detects specific gestures (e.g., bringing index and thumb together) to click.
* **Right Click:** Detects gesture for context menu.
* **Scroll Mode:** Vertical hand movement for scrolling pages.
* **Frame Rate:** Optimized to run smoothly on standard CPUs.

---

## ⚙️ How It Works



1.  **Capture:** The webcam captures the video feed.
2.  **Detection:** **MediaPipe** analyzes the frame to find the hand and its 21 landmarks.
3.  **Processing:** The script checks which fingers are up.
    * *Only Index Up* = **Moving Mode** (Cursor follows finger).
    * *Index + Middle Up* = **Clicking Mode** (Distance between fingers triggers click).
4.  **Action:** **PyAutoGUI** translates these coordinates into OS-level mouse commands.

---

## 🚀 Installation

### Prerequisites
* Python 3.x
* A working Webcam

### Steps
1.  **Clone the repo**
    ```bash
    git clone [https://github.com/Soopaji/hand-controlled-mouse.git](https://github.com/Soopaji/hand-controlled-mouse.git)
    ```
2.  **Navigate to the directory**
    ```bash
    cd hand-controlled-mouse
    ```
3.  **Install dependencies**
    ```bash
    pip install opencv-python mediapipe pyautogui numpy
    ```

---

## 🎮 Usage

Run the main script to start the Virtual Mouse:

```bash
python main.py


Move Cursor: Point with your Index finger.

Click: Bring your Index finger and Thumb together (or Index + Middle, depending on your config).

Quit: Press 'q' to stop the program.
```
🗺️ Roadmap
[x] Basic Cursor Movement

[x] Left & Right Click implementation

[ ] AI-based Smoothing (to reduce jitter)

[ ] Virtual Keyboard integration

🤝 Contributing
Contributions are welcome! If you want to add gesture shortcuts (like "Three fingers to take a screenshot"), feel free to fork and PR.

<div align="center"> <b>Made with ❤️ by <a href="https://www.google.com/search?q=https://github.com/Soopaji">Jai Soopa</a></b> </div>
