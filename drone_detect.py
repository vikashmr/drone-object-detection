import cv2
from ultralytics import YOLO

# 1. Load the AI Model (YOLOv8 Nano - small and fast)
print("📥 Loading AI Model...")
model = YOLO("yolov8n.pt") 

# 2. Open the Webcam (0 is usually the default Mac webcam)
print("📷 Opening Camera...")
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Error: Could not open video source.")
    exit()

print("🚀 Starting Drone Vision System... Press 'q' to quit.")

while True:
    # Read one frame from the camera
    ret, frame = cap.read()
    if not ret:
        break

    # 3. The AI Brain: Detect objects in this frame
    results = model(frame, verbose=False)

    # 4. Draw boxes around the objects
    annotated_frame = results[0].plot()

    # 5. Show the video on screen
    cv2.imshow("Drone Vision Feed", annotated_frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
