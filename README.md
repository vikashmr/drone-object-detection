# Real-time Object Detection (YOLOv8 + OpenCV)

A small real-time computer vision demo: it reads a live video stream (laptop webcam by default), detects objects such as people and vehicles in every frame with YOLOv8, and draws labelled boxes on screen.

Built as a starting point for drone or camera monitoring use cases: the same loop works on any video source OpenCV can open (webcam, video file, RTSP stream).

## How it works
1. OpenCV reads frames from the video source
2. YOLOv8 Nano (`yolov8n.pt`, small and fast) detects objects in each frame
3. The detections are drawn on the frame and shown live; press `q` to quit

## Tech
Python, YOLOv8 (Ultralytics), OpenCV

## Run
```bash
pip install -r requirements.txt
python drone_detect.py
```
To use a video file instead of the webcam, change `cv2.VideoCapture(0)` to `cv2.VideoCapture("video.mp4")`.

## Next steps
- Run on real aerial (drone) footage and measure detection quality
- Fine-tune on an aerial dataset (e.g. VisDrone), since the base model is trained on ground-level images
