import cv2
from ultralytics import YOLO
from datetime import datetime
from alert import generate_alert

# Load pre-trained YOLOv8 model
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

print("Starting Elephant Detection...")
print("Press 'Q' to quit.")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Run YOLO detection
    results = model(frame)

    elephant_detected = False

    # Process detections
    for result in results:

        boxes = result.boxes

        for box in boxes:

            class_id = int(box.cls)
            confidence = float(box.conf)

            label = model.names[class_id]

            if label.lower() == "elephant":

                elephant_detected = True

                print(f"[{datetime.now()}]")
                print(f"Elephant Detected")
                print(f"Confidence : {confidence:.2f}")

                generate_alert(confidence)

    # Draw bounding boxes
    annotated_frame = results[0].plot()

    cv2.imshow("Elephant Detection System", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
