import cv2
import numpy as np
IRGB =cv2.imread("Spiderman.jpg")
print(IRGB)
print(IRGB.shape)
IGS=cv2.cvtColor(IRGB,cv2.COLOR_BGR2GRAY)
print(IGS)
print(IGS.shape)

