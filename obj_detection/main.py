from ultralytics import YOLO
import cv2
import numpy as np
import pyautogui
from playsound import playsound

# Load YOLOv8 model
model = YOLO('yolov8x.pt')

# Initialize plane count
plane_count = 0

# Store the previous position of the plane
previous_centroid = None

# Loop to continuously capture the screen (CCTV camera feed in your case)
while True:
    # Capture the screen (replace this with CCTV camera feed if needed)
    screenshot = pyautogui.screenshot()

    # Convert screenshot to numpy array
    frame = np.array(screenshot)

    # Convert RGB to BGR (OpenCV uses BGR)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Detect and track objects
    results = model.track(frame, persist=True)

    # Iterate over the detected objects
    for result in results:
        for box in result.boxes:
            # Check if the detected object is a plane (assuming class ID for plane is 5, replace with actual ID)
            if box.cls == 5:
                # Increment plane count
                plane_count += 1

                # Play sound notification
                playsound('plane_detected.mp3')

                # Calculate the centroid of the bounding box
                x1, y1, x2, y2 = box.xyxy[0]
                current_centroid = ((x1 + x2) // 2, (y1 + y2) // 2)

                # Determine the direction
                if previous_centroid:
                    direction = "Stationary"
                    if current_centroid[0] > previous_centroid[0]:
                        direction = "Right"
                    elif current_centroid[0] < previous_centroid[0]:
                        direction = "Left"
                    elif current_centroid[1] > previous_centroid[1]:
                        direction = "Down"
                    elif current_centroid[1] < previous_centroid[1]:
                        direction = "Up"

                    # Display direction and plane count on the frame
                    cv2.putText(frame, f"Direction: {direction}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    cv2.putText(frame, f"Planes Detected: {plane_count}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                # Update the previous centroid
                previous_centroid = current_centroid

    # Plot the results
    frame_ = results[0].plot()

    # Visualize the frame
    cv2.imshow('CCTV Plane Detection', frame_)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release resources
cv2.destroyAllWindows()
