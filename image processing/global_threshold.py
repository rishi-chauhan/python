from PIL import Image
import dip_functions

def mean(array, b, e):
    """returns mean of an array"""
    s = 0
    for i in range(b):
        for j in range(e):
            s += array[i][j]
    return s/(b*e)

def binarise_global(image_arr):
    """binarises image, i.e, if pixel values are either 0 or 255"""
    row = image_arr.shape[0]    # get row of the image row
    col = image_arr.shape[1]    # get column of the image row
    m = mean(image_arr, row, col)
    new_image = []
    for r in range(row):
        for c in range(col):
            if image_arr[r,c] <= m:
                new_image.append(0)
            else:
                new_image.append(255)
    im = dip_functions.get_image_from_array(new_image, row, col)
    im.show()

def binarise_local(arr):
    row = arr.shape[0]
    col = arr.shape[1]
    c = 0
    hist = dip_functions.get_hist(arr)

    avg_freq = int(sum(hist)/len(hist))
    for i in range(len(hist)):
        if hist[i] > avg_freq:
            c+=1

    for r in range(row/2):
        for c in range(col/2):
            pass

def main():
    # image_loc = input("Enter image location: ")

    image_original = Image.open("Deg_1.jpg").convert("L")

    # image_original.show()

    image_array = dip_functions.get_image_array(image_original)

    # binariseGlobal(image_array)
    # binariseLocal(image_array)

main()
