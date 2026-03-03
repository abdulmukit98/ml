import cv2
import os
from datetime import datetime

# ==== Settings ====
output_folder = "recordings"
fps = 20.0
frame_width = 640
frame_height = 480
segment_duration = 60 # seconds per video file

# create output folder if not exists
os.makedirs(output_folder, exist_ok=True)

# Open webcam (0 = default canera)
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
cap.set(cv2.CAP_PROP_FPS, fps)

fourcc = cv2.VideoWriter_fourcc(*"XVID")

def create_new_writer():
    timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    filename = os.path.join(output_folder, f"record_{timestamp}.avi")
    return cv2.VideoWriter(filename, fourcc, fps, (frame_width, frame_height))

out = create_new_writer()
start_time = cv2.getTickCount()

window_name = "My_Recordings"
cv2.namedWindow(window_name)

print("Recording started... Press 'q' to stop.")

while True:
    success, frame = cap.read()
    if not success:
        print("Failed to grab frame")
        break

    # flip video
    frame = cv2.flip(frame, 1)
    
    out.write(frame)
    cv2.imshow(window_name, frame)

    # check if segment duration exceed
    elapsed_time = (cv2.getTickCount() - start_time) / cv2.getTickFrequency()
    if elapsed_time > segment_duration:
        out.release()
        out = create_new_writer()
        start_time = cv2.getTickCount()
    
    # stop recording if q pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
        print("Window closed by user.")
        break

cap.release()
out.release()
cv2.destroyAllWindows()
print("Recording stopped.")
