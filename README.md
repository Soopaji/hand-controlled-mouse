<div align="center">

# 🖐️ Gesture Motion Detector

![Python](https://img.shields.io/badge/Python-3670A0?style=plastic&logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=plastic&logo=opencv&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=plastic&logo=pytorch&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow?style=plastic)

<br />

<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjEx.../giphy.gif" alt="Project Demo" width="700"/>

<br />

**A real-time hand gesture recognition system built with Python and Computer Vision.**
<br />
<a href="#-installation">Installation</a> • 
<a href="#-how-it-works">How It Works</a> • 
<a href="#-features">Features</a>

</div>

---

## 📝 About The Project

This project uses **Computer Vision** to track hand movements and translate them into digital commands. The goal is to create a touchless interface that can interpret specific gestures (like waving, pointing, or making a fist) to control applications.

It currently utilizes **MediaPipe/OpenCV** for hand landmarks and **PyTorch** for gesture classification.

## ✨ Features

* **Real-time Detection:** Tracks hand joints at 30+ FPS.
* **Custom Gestures:** Recognizes Swiping, Zooming, and Clicking.
* **Low Latency:** Optimized for standard webcams.
* **Visual Feedback:** Draws skeleton overlays on the video feed.

---

## ⚙️ How It Works



1.  **Input:** Captures video frame from the webcam.
2.  **Preprocessing:** Converts frame to RGB and normalizes data.
3.  **Landmark Extraction:** Detects 21 key points on the hand.
4.  **Classification:** Logic/AI determines which gesture is being formed.
5.  **Action:** Executes the corresponding command (e.g., Volume Up).

---

## 🚀 Installation

Follow these steps to set up the project locally.

### Prerequisites
* Python 3.8+
* Webcam

### Steps
1.  **Clone the repo**
    ```bash
    git clone [https://github.com/Soopaji/Gesture-Motion-Detector.git](https://github.com/Soopaji/Gesture-Motion-Detector.git)
    ```
2.  **Navigate to the directory**
    ```bash
    cd Gesture-Motion-Detector
    ```
3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

---

## 🎮 Usage

Run the main script to start the detection:

```bash
python main.py

Press 'Q' to quit the application.

Press 'D' to toggle debug mode (shows skeleton overlay).

🗺️ Roadmap
[x] Basic Hand Tracking

[x] Finger Counting

[ ] Gesture to Mouse Control

[ ] Integration with Roommate Match App

🤝 Contributing
Contributions are always welcome! If you have a suggestion that would make this better, please fork the repo and create a pull request.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

<div align="center"> <b>Star this repo if you find it useful! ⭐</b> </div>
