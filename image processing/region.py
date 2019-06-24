import dipFuntions
import numpy
from PIL import Image

# get image
image_original = Image.open("T.png").convert("L")
image_original.show()

# get image array
image_arr = dipFuntions.getImageArray(image_original)

# get histogram of image
histogram = dipFuntions.getHist(image_arr)
print histogram

h = []      # to store grayscale values

# store grayscale values
for i in range(256):
    if histogram[i] != 0:
        h.append(i)

# print h

row = image_arr.shape[0]        # get row
col = image_arr.shape[1]        # get column

# segmenting regions
for i in h:
    new_image = []      # for new image
    for r in range(row):
        for c in range(col):
            v = image_arr[r,c]
            if v == i:
                new_image.append(v)
            else:
                new_image.append(255)

    im = dipFuntions.getImageFromArray(new_image, row, col)
    im.show()
