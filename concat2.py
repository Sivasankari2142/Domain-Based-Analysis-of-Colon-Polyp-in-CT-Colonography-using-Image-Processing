import cv2
import numpy as np
img4 = cv2.imread('C:/Users/DELL/projects/colon/final/result4.png')
img5 = cv2.imread('C:/Users/DELL/projects/colon/final/result5.png')
numpy_vertical1=np.vstack((img4,img5))
numpy_vertical_concat1 = np.concatenate((img4,img5), axis=0)
cv2.imwrite('concat2.png', numpy_vertical_concat1)
cv2.waitKey()