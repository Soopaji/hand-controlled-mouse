# Hand → Mouse — Virtual Hand-Controlled Cursor

An experimental Python app that uses your webcam and MediaPipe Hands to control a stylized on-screen cursor with hand gestures. The project shows a live webcam window plus a separate "Virtual Mouse" window that renders an animated multi-cursor visual driven by your index finger and pinch gestures.
## Features
- Real-time hand detection with MediaPipe
- Index-finger → virtual cursor mapping

## Requirements
- Windows (PowerShell instructions below). The app may work on macOS/Linux but was developed and tested on Windows.
# AI Hand Mouse Controller (Pinky Right Click)

Control your OS mouse with a single hand via webcam using MediaPipe landmarks. This project maps the index fingertip to the cursor, uses index+thumb pinch for left click/drag, pinky+thumb pinch for right click, and wrist rotation to trigger scrolling.

## Features
- Cursor movement (index fingertip)
- Left click / drag (index + thumb pinch)
- Right click (pinky + thumb pinch)
- Scroll up/down by rotating the hand
- Live preview window (PyQt5)

## Requirements
- Python 3.8+ (tested on Windows)
- See `requirements.txt` for the main packages

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

If you prefer, install individually:

```bash
python -m pip install opencv-python mediapipe pyautogui PyQt5 numpy
```

## Run

Run the app from the repository root:

```bash
python main.py
```

The app will open a window showing the webcam feed and a status label.

## Controls / Gestures
- Move cursor: move your index finger (tip landmark #8).
- Left click / drag: pinch index + thumb (tips #8 and #4). A short pinch issues mouseDown(); release issues mouseUp().
- Right click: pinch pinky + thumb (tips #20 and #4).
- Scroll: rotate your wrist relative to the middle knuckle (angle computed between landmarks #0 and #9). Rotating beyond configured deadzones scrolls up/down.

## Tuning
You can edit these values in `main.py` to adjust sensitivity:
- `pinch_threshold` (default 0.05) — distance threshold for detecting pinches (normalized coordinates)
- `smoothing` (default 0.15) — cursor smoothing (0 = instant, higher = more smoothing)
- `margin` (default 0.15) — active area margin in the camera frame
- `angle_deadzone_min` / `angle_deadzone_max` — angle thresholds for scroll activation
- `scroll_speed` — lines to scroll per scroll event

## Safety & Notes
- `pyautogui.FAILSAFE` is disabled in the code; this prevents the built-in corner emergency stop. Be careful while testing — the mouse will move.
- If you want a safe test mode, comment out `pyautogui` calls in `move_mouse()` or re-enable failsafe.
- The app uses the first webcam (index 0) and uses DirectShow on Windows (`cv2.CAP_DSHOW`).
- If the GUI doesn't start, ensure `PyQt5` is installed and that you are running the script in a desktop session.

## Troubleshooting
- Camera not found: try another index or remove `cv2.CAP_DSHOW`.
- Actions missing: verify MediaPipe detects your hand (check the video preview) and tune `pinch_threshold`.
- Permission issues (Windows): run the terminal as the same user and allow camera access.

## Next steps (optional)
- Add a `--dry-run` flag to preview gestures without sending `pyautogui` events.
- Expose tuning parameters via CLI or a small settings UI.
- Add logging for dropped frames and `pyautogui` exceptions.

## CLI options
`main.py` now accepts optional command-line flags to tune behavior and enable a dry-run mode that prevents actual mouse events (useful for testing).

Examples:

```bash
# run normally (default)
python main.py

# dry-run: preview gestures without moving the system mouse
python main.py --dry-run

# tune sensitivity and smoothing
python main.py --pinch-threshold 0.04 --smoothing 0.12 --margin 0.12

# tune scroll behavior
python main.py --scroll-speed 60 --angle-deadzone-min -120 --angle-deadzone-max -60
```

Flags:
- `--dry-run` : if present, disables calls to `pyautogui` (no mouse movement/clicks).
- `--pinch-threshold FLOAT` : pinch distance threshold (normalized units, default 0.05).
- `--smoothing FLOAT` : cursor smoothing factor (default 0.15).
- `--margin FLOAT` : camera active-area margin (default 0.15).
- `--scroll-speed INT` : scroll amount per tick (default 40).
- `--angle-deadzone-min FLOAT`, `--angle-deadzone-max FLOAT` : angle thresholds for scroll activation.

---
Created for the `main.py` controller in this repo.


Inspired by tubakhxn/hand-mouse-controll

clone my repo:
git clone https://github.com/Soopaji/hand-controlled-mouse.git
