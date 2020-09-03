import cv2
import matplotlib.pyplot as plt
raw_image = cv2.imread('C:/Users/DELL/projects/images/46.png')
bilateral_filtered_image = cv2.bilateralFilter(raw_image, 5, 175, 175)
edge_detected_image = cv2.Canny(bilateral_filtered_image, 75, 200)
cv2.imwrite('edged.png',edge_detected_image)
contours, hierarchy = cv2.findContours(edge_detected_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contour_list = []
for contour in contours:
    approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    area = cv2.contourArea(contour)
    if ((len(approx) > 8) & (len(approx) < 23) & (area > 30) ):
        contour_list.append(contour)
cv2.drawContours(raw_image, contour_list,  -1, (255,0,0), 2)
cv2.imwrite('object.png',raw_image)
cv2.waitKey(0)