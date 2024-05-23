import cv2
import math
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors

model = YOLO("yolov8s.pt")
cap = cv2.VideoCapture("Y2meta.app - Shopping, People, Commerce, Mall, Many, Crowd, Walking   Free Stock video footage   YouTube.mp4")

w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

out = cv2.VideoWriter('visioneye-distance-calculation.avi', cv2.VideoWriter_fourcc(*'MJPG'), fps, (w, h))

center_point = (623, 709)
pixel_per_meter = 10

txt_color, txt_background, bbox_clr = ((0, 0, 0), (255, 255, 255), (255, 0, 0))

while True:
    ret, im0 = cap.read()
    if not ret:
        print("Video frame is empty or video processing has been successfully completed.")
        break

    annotator = Annotator(im0, line_width=2)

    results = model.track(im0, persist=True)
    boxes = results[0].boxes.xyxy.cpu()

    if results[0].boxes.id is not None:
        track_ids = results[0].boxes.id.int().cpu().tolist()

        for box, track_id in zip(boxes, track_ids):
            x1, y1 = int((box[0] + box[2]) // 2), int((box[1] + box[3]) // 2)
            distance = (math.sqrt((x1 - center_point[0]) ** 2 + (y1 - center_point[1]) ** 2))/pixel_per_meter
            if(distance<30):
                bbox_clr=(0,0,255)
            

            text_size, _ = cv2.getTextSize(f"Distance: {distance:.2f} m", cv2.FONT_HERSHEY_SIMPLEX,0.5, 1)
            cv2.rectangle(im0, (x1, y1 - text_size[1] - 10),(x1 + text_size[0] + 10, y1), txt_background, -1)
            if(distance<30):
                cv2.putText(im0, f"Threat: {distance:.2f} m", (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                annotator.box_label(box, label=str(track_id),color=(0,0,255))
                annotator.visioneye(box, center_point)
            else:
                annotator.box_label(box, label=str(track_id),color=(255,0,0))
                annotator.visioneye(box, center_point)
                cv2.putText(im0, f"Distance:{distance:.2f} m",(x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,txt_color, 1)

    out.write(im0)
    cv2.imshow("visioneye-distance-calculation", im0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

out.release()
cap.release()
cv2.destroyAllWindows()