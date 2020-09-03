# import Pillow modules

from PIL import Image
import matplotlib.pyplot as plt
from PIL import ImageFilter
img1 = Image.open("C:/Users/DELL/projects/colon/original.png");
for i in range(0, img1.size[0]-1):
	for j in range(0, img1.size[1]-1):
        	pixelColorVals = img1.getpixel((i,j));
        	# Invert color

        	redPixel    = 255 - pixelColorVals[0]; # Negate red pixel

        	greenPixel  = 255 - pixelColorVals[1]; # Negate green pixel

        	bluePixel   = 255 - pixelColorVals[2]; # Negate blue pixel
        	# Modify the image with the inverted pixel values

        	img1.putpixel((i,j),(redPixel, greenPixel, bluePixel));

# Display the negative image
img1.save('negate0.png');

