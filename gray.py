import cv2  
image = cv2.imread('C:/Users/DELL/projects/colon/original.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray.png',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()