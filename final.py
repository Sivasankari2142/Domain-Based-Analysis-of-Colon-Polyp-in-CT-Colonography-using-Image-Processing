import cv2
import numpy as np
import sample
import demo
import measure
import gray
import blur
import negate
import negate1
import gradient
import arrange
import concat
import concat1
import concat2
img = cv2.imread('C:/Users/DELL/projects/colon/final/concat.png')
img1 = cv2.imread('C:/Users/DELL/projects/colon/final/concat1.png')
img2=cv2.imread('C:/Users/DELL/projects/colon/final/concat2.png')
numpy_horizontal = np.hstack((img, img1,img2))
numpy_horizontal_concat = np.concatenate((img,img1,img2), axis=0)
cv2.imwrite('final.png', numpy_horizontal_concat)
cv2.imshow('Final Outputs',numpy_horizontal_concat)
cv2.waitKey()
