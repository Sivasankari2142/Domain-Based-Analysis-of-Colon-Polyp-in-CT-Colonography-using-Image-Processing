from PIL import Image
import matplotlib.pyplot as plt
def getRed(redVal):
    return '#%02x%02x%02x' % (redVal, 0, 0)
def getGreen(greenVal):
    return '#%02x%02x%02x' % (0, greenVal, 0)
def getBlue(blueVal):
    return '#%02x%02x%02x' % (0, 0, blueVal)
image = Image.open("C:/Users/DELL/projects/colon/original.png")
image.putpixel((0,1), (1,1,5))
image.putpixel((0,2), (2,1,5))
histogram = image.histogram()
l1 = histogram[0:256]
l2 = histogram[256:512]
l3 = histogram[512:768]
plt.figure(0)
plt.title("Red pixels")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
# R histogram
for i in range(0, 256):
	plt.bar(i, l1[i], color = getRed(i), edgecolor=getRed(i), alpha=0.3)
# G histogram
plt.savefig('histogram2.png')
plt.figure(1)
plt.title("Green pixels")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
for i in range(0, 256):
	plt.bar(i, l2[i], color = getGreen(i), edgecolor=getGreen(i),alpha=0.3)
# B histogram
plt.savefig('histogram1.png')
plt.figure(2)
plt.title("Blue pixels")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
for i in range(0, 256):
    plt.bar(i, l3[i], color = getBlue(i), edgecolor=getBlue(i),alpha=0.3)

plt.savefig('histogram.png')

 

