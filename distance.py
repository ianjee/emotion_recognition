import cv2
import numpy as np

# Define the size of the reference object (in this example, the size of your face in meters)
reference_object_size = 0.15  # Assuming your face is approximately 15 cm wide

# Calibrated focal length of the camera (obtained from camera calibration)
focal_length = 1000  # Example value, replace with actual calibrated value

# Function to calculate distance from camera to object
def calculate_distance(known_width, focal_length, per_width):
    # Calculate the distance using the formula: distance = (known_width * focal_length) / per_width
    distance = (known_width * focal_length) / per_width
    return distance

# Start the webcam feed
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Detect faces in the frame
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Calculate the distance to the face
    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        # Calculate the distance to the face
        distance = calculate_distance(reference_object_size, focal_length, w)

        # Display the distance on the frame
        cv2.putText(frame, f'Distance: {distance:.2f} meters', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Frame', frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()
