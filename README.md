# 👁️ Eye Pattern Detection System for Computer Access

This project implements an iris detection and tracking system using **OpenCV**, designed to interpret eye blinks as a binary sequence. The system decodes this sequence into a numeric password that can unlock access to the computer, enabling a hands-free biometric interface based on ocular gestures (More technical details are provided in Informe Proyecto.pdf).

---

## 🧠 Technical Overview

- **Image Processing**: Grayscale conversion, face detection, Region of Interest (ROI) reduction, Gaussian filtering.
- **Iris Detection**: Edge detection using Canny + Hough Circle Transform for accurate iris localization.
- **Eye Tracking**: Real-time overlay:
  - 🟢 Green circles for valid pupil detections
  - 🔴 Red dot indicating the iris center
- **Blink-to-Binary Input**: Interprets eye blinks as binary digits (`1` or `0`), forming a password.
- **Password Validation**: Matches the detected binary sequence with a predefined password.
- **Real-Time Visualization**: Webcam feed with graphical overlay and status updates.

---

## 📸 Demo

🎥 [Watch the demo video](demo/video_demo.mp4)

---

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/miguelangelhuamani/CV_FinalProject.git
   cd cv-final-project
   ```

2. Install the required packages:
	```bash
	pip install -r requirements.txt
	```

3. Choose your input method:

	**Option A: Run with a sample video**: Place a test video inside the input/ folder and name it video.mp4. Then run:

	```bash
	python src/main.py
	```


	**Option B: Run with your webcam**: Open the file src/main.py and replace the following line:

	`cap = cargar_video("./input/video.mp4")`

	with:

	`cap = cv2.VideoCapture(0)`

	Then run:

	```bash
	python src/main.py
	```
	


