import cv2
import numpy as np

def draw_circle(event,x,y,flags,param):
    global PNT1
    global PNT2
    global EVT
    if event == cv2.EVENT_LBUTTONDOWN:
        PNT1 = (x,y)
        EVT = event
        print(event)
    if event == cv2.EVENT_LBUTTONUP:
        PNT2=(x,y)
        EVT = event

cv2.namedWindow("image")
cv2.setMouseCallback("image",draw_circle)

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True: