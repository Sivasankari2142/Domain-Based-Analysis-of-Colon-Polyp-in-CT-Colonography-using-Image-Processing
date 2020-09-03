import cv2
import numpy as np
img2 = cv2.imread('C:/Users/DELL/projects/colon/final/result2.png')
img3 = cv2.imread('C:/Users/DELL/projects/colon/final/result3.png')
numpy_vertical = np.vstack((img2,img3))
numpy_vertical_concat = np.concatenate((img2,img3), axis=0)
cv2.imwrite('concat1.png',numpy_vertical_concat)
cv2.waitKey()
