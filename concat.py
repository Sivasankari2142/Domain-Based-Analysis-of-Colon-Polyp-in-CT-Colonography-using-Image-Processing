import cv2
import numpy as np
img = cv2.imread('C:/Users/DELL/projects/colon/final/result.png')
img1 = cv2.imread('C:/Users/DELL/projects/colon/final/result1.png')
numpy_vertical = np.vstack((img,img1))
numpy_vertical_concat = np.concatenate((img,img1), axis=0)
cv2.imwrite('concat.png',numpy_vertical_concat)
cv2.waitKey()