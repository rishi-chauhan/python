"""
The following code uses concept of stegography and hides text entered in the
specified image by replacing LSB of each pixel
"""
import sys                   # to get size of text
from PIL import Image       # for image related operations
import numpy                # for array handling
import dip_functions          # for self-written functions

def hide(img_array, txt):
    """hide text into image"""
    row = img_array.shape[0]    # get row of the image row
    col = img_array.shape[1]    # get column of the image row
    txt_bin = []                # this stores list of lists of text converted into binary
    text1 = []                  # list to store binary array of the text
    new_image_array = []        # list to store changed value pixels of new image
    count = 0                   # counts number of iterations

    # convert text into binary
    for i in txt:
        txt_bin.append(list(bin(ord(i))[2:]))   # store text converted into binary in a list

    # convert list of lists into a list
    for i in txt_bin:
        for j in i:
            text1.append(j)

    # hide begins :)
    for r in range(row):
        for t in range(col):
            # if number of iterations are less than the length of text1
            if count <= len(text1)-1:
                # convert pixel value into binary and make a list of it
                a = list(bin(img_array[r, t]))
                # replace LSB with text bit
                a[len(a)-1] = text1[t]
                a = "".join(a)
                # store updated value in array
                new_image_array.append(int(a, 2))
                count += 1
            else:
                # store the unchanged value
                new_image_array.append(img_array[r, t])
    # converting list into array
    new_image_array = numpy.array(new_image_array)
    # reshaping array
    new_image_array = new_image_array.reshape(img_array.shape[0], img_array.shape[1])
    return new_image_array, len(text1)

def unhide(img_array, txt):
    """extract text from image"""
    row = img_array.shape[0]    # get row of the image row
    col = img_array.shape[1]    # get column of the image row
    ans = []                    # this stores intermediate answer
    count = 0                   # counts iterations till len(txt)

    # extraction begins :)
    for r in range(row):
        for t in range(col):
            # if number of iterations are less than the length of txt
            if count <= txt-1:
                # get pixel value and convert into binary
                a = list(bin(img_array[r, t]))
                # store LSB in a list
                ans.append(a[len(a)-1])
                count += 1
    b = ""      # empty string
    c = []      # list to store converted data
    # iterate through the ans list and convert binary to char
    for i in range(len(ans)):
        b += ans[i]
        # if length of b == 7 because we are storing 7 bits (as we are excluding "0b") in hide()
        # then break the string at 7
        if len(b) == 7:
            b = "0b"+b
            # store the converted binary to string in list c
            c.append(chr(int(b, 2)))
            b = ""

    return c

def main():

    # get text from user
    text = input("Enter the text you want to hide: ")

    # get image location from user
    image_loc = input("Enter the path of the image: ")

    # load the image and then convert it into greyscale
    image_original = Image.open(image_loc).convert("L")

    # display the original image
    image_original.show()

    # get the array of the image
    image_array = dip_functions.get_image_array(image_original)

    # amount of data that can be hidden
    # here we divide by 7 because we are considering only 7 bits by excluding "0b"
    h = ((image_array.shape[0] * image_array.shape[1])/7)
    print("Amount of data that can be hidden is: ", h, "B")

    # get size of image in B
    txt_size = sys.getsizeof(text)

    # if data can be hidden
    if txt_size <= h:
        # hide data and get image array and hidden text
        im_new, text_size = hide(image_array, text)

        # get updated image
        im = Image.fromarray(numpy.uint8(im_new))
        # get updated image
        im.show()

        # unhide data
        extracted_text = unhide(dip_functions.get_image_array(im),text_size)

        # print hidden data
        t = "".join(extracted_text)
        print("The extracted text is:", t)

    # if data cannot be hidden
    else:
        print("Text size is large than amount of data that can be hidden in the image.")

main()
