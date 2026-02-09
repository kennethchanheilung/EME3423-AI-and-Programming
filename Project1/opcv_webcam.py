import cv2
import numpy as np

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    _, img = cam.read()
    imgCanny = cv2.Canny(img,100,100)

    kernel = np.ones((3,3), np.uint8)
    imgDilation = cv2.dilate(imgCanny , kernel,  iterations= 1)

    cv2.imshow("webcam", img)
    cv2.imshow("Canny", imgCanny)
    cv2.imshow("Dilate", imgDilation)

    key = cv2.waitKey(20) & 0xff
    if key == ord("q") or key == 27:
        break

cam.release()
cv2.destroyAllWindows()