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

# Variables for background subtraction
first_frame = None
gun_detected = False

while True:
    ret, frame = camera.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Resize the frame for consistency
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Gun detection
    guns = gun_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around detected guns
    for (x, y, w, h) in guns:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        gun_detected = True  # Set flag if gun is detected

    # Overlay detection result
    if gun_detected:
        cv2.putText(frame, "Gun Detected!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    else:
        cv2.putText(frame, "No Gun Detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the result
    cv2.imshow("Gun Detection", frame)

    # Break loop on 'q' key press
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# Final detection result
if gun_detected:
    print("Gun detected!")
else:
    print("No gun detected!")

# Release resources
camera.release()
cv2.destroyAllWindows()
