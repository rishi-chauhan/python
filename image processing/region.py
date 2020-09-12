from PIL import Image
import dip_functions

# get image
IMAGE_ORIGINAL = Image.open("T.png").convert("L")
IMAGE_ORIGINAL.show()

# get image array
IMAGE_ARR = dip_functions.get_image_array(IMAGE_ORIGINAL)

# get histogram of image
HISTOGRAM = dip_functions.get_hist(IMAGE_ARR)
print(HISTOGRAM)

h = []      # to store grayscale values

# store grayscale values
for i in range(256):
    if HISTOGRAM[i] != 0:
        h.append(i)

# print h

ROW = IMAGE_ARR.shape[0]        # get row
COL = IMAGE_ARR.shape[1]        # get column

# segmenting regions
for i in h:
    new_image = []      # for new image
    for r in range(ROW):
        for c in range(COL):
            v = IMAGE_ARR[r, c]
            if v == i:
                new_image.append(v)
            else:
                new_image.append(255)

    im = dip_functions.get_image_from_array(new_image, ROW, COL)
    im.show()
