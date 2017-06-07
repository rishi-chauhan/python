from PIL import Image
import numpy
import dipFuntions

def mean(array, b, e):
    s = 0
    for i in range(b):
        for j in range(e):
            s += array[i][j]
    return s/(b*e)

def binariseGlobal(image_arr):
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
    im = dipFuntions.getImageFromArray(new_image, row, col)
    im.show()

def binariseLocal(arr):
    row = arr.shape[0]
    col = arr.shape[1]
    c=0
    hist= dipFuntions.getHist(arr)

    avg_freq= int(sum(hist)/len(hist))
    for i in range(len(hist)):
        if hist[i]>avg_freq:
            c+=1

    for r in range(row/2):
        for c in range(col/2):

def main():
    # image_loc = input("Enter image location: ")

    image_original = Image.open("Deg_1.jpg").convert("L")

    # image_original.show()

    image_array = dipFuntions.getImageArray(image_original)

    # binariseGlobal(image_array)
    # binariseLocal(image_array)

main()
