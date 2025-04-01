# 🔫 Gun Detection System Using OpenCV 🔫

## Overview

This Python script utilizes OpenCV and a pre-trained Haar Cascade Classifier to detect the presence of guns in real-time through a webcam feed. The system continuously monitors the video stream, highlighting detected guns with bounding boxes and providing a real-time status message on the screen.

## Features

- **Real-Time Detection:** Processes live webcam footage for immediate gun detection.
- **Haar Cascade Classifier:** Uses a pre-trained model for accurate object detection.
- **Visual Feedback:** Displays bounding boxes around detected guns with status messages.
- **Simple Interface:** Easy to run with minimal setup.

## Requirements

- **Python 3.x**
- **OpenCV (`cv2`)** - Install via `pip install opencv-python`
- **NumPy (`numpy`)** - Install via `pip install numpy`
- **Haar Cascade XML File (`cascade.xml`)** - A pre-trained classifier for gun detection.

## How It Works

1. **Webcam Initialization:** The script accesses the default webcam to capture live video frames.
2. **Preprocessing:** Each frame is resized and converted to grayscale for efficient processing.
3. **Gun Detection:** The Haar Cascade Classifier scans the frame to detect guns.
4. **Annotation:** Bounding boxes are drawn around detected guns, and status messages are displayed.
5. **Real-Time Monitoring:** The detection loop continues until the user presses the 'q' key to quit.

## Installation

1. **Clone the Repository (optional):**

```bash
git clone https://github.com/yourusername/gun-detection.git
cd gun-detection
```

2. **Install Dependencies:**

```bash
pip install opencv-python numpy imutils
```

3. **Ensure the Haar Cascade File (`cascade.xml`) is in the same directory as the script.**  
   - If you don't have `cascade.xml`, you'll need to train a classifier or download a pre-trained model.

## Usage

```bash
python gun_detection.py
```

- **Real-Time Display:** The video feed will appear in a window named "Gun Detection."
- **Status Messages:** "Gun Detected!" will appear if a gun is detected, otherwise "No Gun Detected."
- **Exit:** Press the 'q' key to terminate the script.

## Example Output

![Gun Detection Example](example_output.png) *(Add a sample screenshot if available)*

- **Green Rectangle & Text:** No gun detected.
- **Red Rectangle & Text:** Gun detected.

## Sample Code

```python
import numpy as np
import cv2
import imutils

# Load the pre-trained Haar cascade for gun detection
gun_cascade = cv2.CascadeClassifier('cascade.xml')

# Initialize the webcam
camera = cv2.VideoCapture(0)
if not camera.isOpened():
    print("Error: Could not open webcam.")
    exit()

gun_detected = False

while True:
    ret, frame = camera.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    guns = gun_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in guns:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        gun_detected = True

    cv2.putText(frame, "Gun Detected!" if gun_detected else "No Gun Detected", 
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255 if gun_detected else 0), 2)

    cv2.imshow("Gun Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
```

## Notes

- **Accuracy:** The detection performance depends on the quality of the `cascade.xml` file. For improved accuracy, consider training a custom Haar Cascade or using deep learning models (e.g., YOLO, SSD).
- **Safety:** This script is for educational and research purposes only. Always follow legal and ethical guidelines when implementing security-related applications.

## License

This project is licensed under the MIT License. Feel free to modify and use it for educational or research purposes.

---
