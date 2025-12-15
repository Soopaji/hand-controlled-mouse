
░█████╗░███████╗████████╗██╗░░██╗███████╗██████╗░
██╔══██╗██╔════╝╚══██╔══╝██║░░██║██╔════╝██╔══██╗
███████║█████╗░░░░░██║░░░███████║█████╗░░██████╔╝
██╔══██║██╔══╝░░░░░██║░░░██╔══██║██╔══╝░░██╔══██╗
██║░░██║███████╗░░░██║░░░██║░░██║███████╗██║░░██║
╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝

░█████╗░██╗░░░██╗██████╗░░██████╗░██████╗░██████╗░
██╔══██╗██║░░░██║██╔══██╗██╔════╝██╔═══██╗██╔══██╗
██║░░╚═╝██║░░░██║██████╔╝╚█████╗░██║░░░██║██████╔╝
██║░░██╗██║░░░██║██╔══██╗░╚═══██╗██║░░░██║██╔══██╗
╚█████╔╝╚██████╔╝██║░░██║██████╔╝╚██████╔╝██║░░██║
░╚════╝░░╚═════╝░╚═╝░░╚═╝╚═════╝░░╚═════╝░╚═╝░░╚═╝
````

> *The Zero-Touch Interface Protocol*

-----

\<div align="center"\>

[](https://github.com/)
[](https://github.com/)
[](https://github.com/)
[](https://www.google.com/search?q=)

\</div\>

-----

## 🟢 The Mission

**Aether Cursor** abandons the physical mouse, turning your webcam into a high-precision sensor array. By tracking the skeletal geometry of your hand, it allows you to manipulate your digital environment through pure movement.

This project maps your index fingertip to the cursor, uses pinch gestures for clicks, and gyroscopic hand rotation for scrolling.

**Status:** *Experimental Python App / Windows Optimized.*

-----

## ⚡ The Control Schematic

*Master the gestures to master the machine.*

```mermaid
graph TD;
    HAND_DETECTED -->|Analyze Geometry| ACTION;
    ACTION -->|Index Point| CURSOR_MOVE;
    ACTION -->|Index + Thumb Pinch| LEFT_CLICK_DRAG;
    ACTION -->|Pinky + Thumb Pinch| RIGHT_CLICK;
    ACTION -->|Wrist Rotate Left/Right| SCROLL_WHEEL;
    STYLE HAND_DETECTED fill:#222,stroke:#00ffcc,stroke-width:2px,color:#fff
    STYLE ACTION fill:#222,stroke:#fff,stroke-width:1px,color:#fff
    STYLE CURSOR_MOVE fill:#333,stroke:#00ffcc,color:#00ffcc
    STYLE LEFT_CLICK_DRAG fill:#333,stroke:red,color:red
    STYLE RIGHT_CLICK fill:#333,stroke:magenta,color:magenta
    STYLE SCROLL_WHEEL fill:#333,stroke:orange,color:orange
```

### 🎮 Gesture Protocol

| Gesture | Action | The Logic |
| :--- | :--- | :--- |
| **The Point** | **Move Cursor** | Your Index Finger (Landmark \#8) controls the XY position. |
| **The Pinch** | **Left Click / Drag** | **Index + Thumb**. Short pinch = Click. Hold pinch = Drag. |
| **The Snap** | **Right Click** | **Pinky + Thumb**. A distinct pinch for context menus. |
| **The Dial** | **Scroll** | **Rotate your Hand** relative to the knuckle.<br>• **Tilt Left:** Scroll Up<br>• **Tilt Right:** Scroll Down |

-----

## 🛠️ Deployment Sequence

### 1\. Acquire Source

Clone the repository to your local terminal:

```bash
git clone [https://github.com/Soopaji/hand-controlled-mouse.git](https://github.com/Soopaji/hand-controlled-mouse.git)
cd hand-controlled-mouse
```

### 2\. Prerequisite Systems

Initialize Python 3.8+ and the visual processing arrays.

```bash
# Automatic Install
python -m pip install -r requirements.txt

# Manual Install
python -m pip install opencv-python mediapipe pyautogui PyQt5 numpy
```

### 3\. Initiate The Link

Launch the neural interface:

```bash
python main.py
```

*A HUD window will appear displaying the camera feed with the skeletal overlay. Align your hand within the safety frame.*

-----

## ⚙️ Advanced Configuration (CLI)

The system accepts command-line flags to tune the physics engine or run in safety mode.

| Flag | Argument | Description |
| :--- | :--- | :--- |
| `--dry-run` | *None* | **Simulation Mode.** Disables actual mouse movement/clicks. Useful for testing gesture detection safely. |
| `--pinch-threshold` | `FLOAT` | How close fingers must be to "Click" (Normalized 0.0-1.0). Default: `0.05`. |
| `--smoothing` | `FLOAT` | The "Drift" factor. Lower is smoother/slower. Default: `0.15`. |
| `--margin` | `FLOAT` | The "Zoom". Active area margin in camera frame. Default: `0.15`. |
| `--scroll-speed` | `INT` | Lines to scroll per event. Default: `40`. |
| `--angle-deadzone-min` | `FLOAT` | Angle to trigger Scroll UP. Default: `-110`. |
| `--angle-deadzone-max` | `FLOAT` | Angle to trigger Scroll DOWN. Default: `-70`. |

**Example Launch:**

```bash
# High sensitivity mode with scroll tuning
python main.py --pinch-threshold 0.04 --smoothing 0.10 --scroll-speed 60
```

-----

## ⚠️ Safety Protocols & Troubleshooting

  * **Failsafe Override:** `pyautogui.FAILSAFE` is **DISABLED** to prevent crashes when reaching screen corners. Be careful; the mouse *will* move. Use `--dry-run` to test first.
  * **Lighting:** The system thrives in illuminated environments. Darkness will degrade signal quality.
  * **Camera Conflicts:** The app uses `cv2.CAP_DSHOW` (DirectShow) for faster Windows access. If your camera fails to load, remove this flag in the code or try a different index.
  * **Permissions:** Ensure your terminal has permission to control input devices (especially on macOS).

-----

\<div align="center"\>

> *"The tool is merely an extension of the hand."*

**[ END OF LINE ]**

<br>

\<sub\>Inspired by \<a href="https://www.google.com/search?q=https://github.com/tubakhxn/hand-mouse-controll"\>tubakhxn/hand-mouse-controll\</a\>\</sub\>

\</div\>

```
```
