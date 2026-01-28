import cv2

print("OPenCV Version : " + cv2.__version__)

img = cv2.imread('Resources/cat_large.jpg')

print(img.shape)

img = cv2.resize(img, (int(img.shape[1]/1.5),int(img.shape[0]/1.5)))

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)

cv2.imshow("Frame",img)

cv2.waitKey(0)