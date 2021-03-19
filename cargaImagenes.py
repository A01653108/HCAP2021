import cv2
import numpy as np
IRGB = cv2.imread("Spiderman.jpg")
print(IRGB)
print(IRGB.shape)
print("Lineas agrgadas en la rama2")
IGS=cv2.cvtColor(IRGB,cv2.COLOR_BGR2GRAY)
print(IGS)
print(IGS.shape)
cv2.imwrite("Spiderman.jpg,IGS)

