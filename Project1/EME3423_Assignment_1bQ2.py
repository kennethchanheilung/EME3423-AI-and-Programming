import cv2
import numpy as np

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while  True:
    _ , img = cam.read()

    img1 = cv2.Canny(img,100,100)
    img2 = img
    img3 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img4 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    kernel = np.ones((3,3), np.uint8)
    imgDilation = cv2.dilate(img4, kernel, iterations=1)
    cv2.imshow("img1",img1)
    cv2.imshow("img2", img2)
    cv2.imshow("img3", img3)
    cv2.imshow("img4", img4)

    key = cv2.waitKey(20) & 0xff
    if key == ord("q") or key == 27:
        break

cam.release()
cv2.destroyAllWindows()