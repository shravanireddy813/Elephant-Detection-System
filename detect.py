from ultralytics import YOLO

model = YOLO("best.pt")      # Your trained elephant detection model

results = model("image.png")

for result in results:
    boxes = result.boxes

    for box in boxes:
        cls = int(box.cls)

        label = model.names[cls]

        confidence = float(box.conf)

        if label.lower() == "elephant":
            print(f"🐘 Elephant Detected! Confidence: {confidence:.2f}")
            print("🚨 Alert: Elephant detected near the monitored area!")

result.show()
