import cv2 
import numpy as np 
import matplotlib.pyplot as plt
image = cv2.imread('C://Users//DELL//projects//colon//original.png') 
Gaussian = cv2.GaussianBlur(image, (7, 7), 0) 
plt.imshow(Gaussian)
plt.title('Gaussian Blur')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.savefig('gaussian.png')
cv2.waitKey(0) 