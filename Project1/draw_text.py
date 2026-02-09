import cv2
import numpy as np

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    _, img = cam.read()
    imgCanny = cv2.Canny(img,100,100)

    kernel = np.ones((3,3), np.uint8)
    imgDilation = cv2.dilate(imgCanny , kernel,  iterations= 1)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,"This is a cat.",(10,100),font,1,(255,255,255),2)
    cv2.putText(imgCanny,"This is a cat.",(10,100),font,1,(255,255,255),2)
    cv2.putText(imgDilation,"This is a cat.",(10,100),font,1,(255,255,255),2)

    cv2.imshow("webcam", img)
    cv2.imshow("Canny", imgCanny)
    cv2.imshow("Dilate", imgDilation)

    if cv2.waitKey(20) & 0xff == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()

# capture = cv2.VideoCapture('Resources/kitten.mp4')
#
# while True:
#     success, img = capture.read()
#
#     font = cv2.FONT_HERSHEY_SIMPLEX
#     cv2.putText(img,"This is a cat.",(10,100),font,1,(255,255,255),2)
#
#     cv2.imshow("img",img)
#
#     if cv2.waitKey(20) & 0xff == ord("q"):
#         break
#
# capture.release()
# cv2.destroyAllWindows()

# img = cv2.imread("Resources/cat_large.jpg")
#
# img = cv2.resize(img, (int(img.shape[1]/1.5),int(img.shape[0]/2)))
#
# font = cv2.FONT_HERSHEY_SIMPLEX
# cv2.putText(img,"This is a cat.",(10,100),font,1,(255,255,255),2)
#
# # img = np.zeros((500,500,3),np.uint8)
# #
# # img = cv2.line(img,(0,0),(500,500),(255,0,0),5)
# # img = cv2.circle(img,(300,200),50,(0,255,0),0)
# cv2.imshow("img",img)
#
# cv2.waitKey(0)