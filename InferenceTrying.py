import cv2
import torch
import torch.nn as nn
import numpy as np

# cap = cv2.VideoCapture(0)
# while True:
#     res, frame = cap.read()
#     cv2.imshow('frame', frame)

#     key = cv2.waitKey(1)
#     if key == 27:
#         break

# cap.release()
# cv2.destroyAllWindows()

model = torch.load('./best.pt')
model.eval()

for param in model.parameters():
    print(param.data)