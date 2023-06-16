import torch
import numpy as np
import cv2

model = torch.hub.load('ultralytics/yolov5','custom',path='redemption5.pt',force_reload=True)

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret,frame = cap.read()
    result = model(frame)

    cv2.imshow('Yolo',np.squeeze(result.render()))

    if cv2.waitKey(10) & 0xff == ord('z'):
        break

cap.release()
cv2.destroyAllWindows()