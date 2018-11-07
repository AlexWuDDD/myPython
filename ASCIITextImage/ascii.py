import sys, random, argparse
import numpy as np
import math
from PIL import Image

# 70 levels of gray
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

# 10 levels of gray
gscale2 = " .:-=+*#%@"
gscale2 = gscale2[::-1]
print(gscale2)


def covertImageToAscii(fileName, cols, scale, moreLevels):
    """Given Image and dimensions(rows, cols), return an m*n list of Images"""
    # declare globals
    global gscale1, gscale2

    # open the image and convert to grayscale
    image = Image.open(fileName).convert("L") # Image.convert()将该图像转换为灰度图像，"L"代表luminance,是图像亮度的单位
    # store the image dimensions
    W, H = image.size[0], image.size[1]
    # compute the tile width
    w = W / cols  # cols用户指定的列数
    # compute the tile height based on the aspect ratio and scale of the font
    h = w / scale # 垂直比例系数
    # compute the number of rows to use in the final grid
    rows = int(H/h)

    print("cols: %d, wors: %d" % (cols, rows))
    print("tile dims: %d x %d" % (w, h))

    # check if image size is too small
    if cols > W or rows > H:
        print("Image too small for specified cols")
        exit(0)

    # an ASCII image is a list of character strings
    aimg = []
    # generate the list of tile dimensions
    for j in range(rows):
        y1 = int(j * h)
        y2 = int((j + 1) * h)
        # correct the last tile
        if h == rows - 1:
            y2 = H
        # append an empty string
        aimg.append("")
        for i in range(cols):
            # corp the image to fit the tile
            x1 = int(i * w)
            x2 = int((i + 1) * w)
            # correct the last tile
            if i == cols - 1:
                x2 = W
            # corp the image to extract the tile into another Image object
            img = image.crop((x1, y1, x2, y2))
            # get the average luminance
            avg = int(getAverageL(img))
            # look up the ACSII character for grayscale value(avg)
            if moreLevels:
                gsval = gscale1[int((avg * 69) / 255)]
            else:
                gsval = gscale2[int((avg * 9) / 255)]
            # append the ASCII character to the string
            aimg[j] += gsval
    return aimg


def getAverageL(image):
    # get the image as a numpy array
    im = np.array(image)
    # get the dimensions
    w, h = im.shape
    # get the avaerage
    return np.average(im.reshape(w*h))


def main():
    imgFile = 'robot.jpg'
    outFile = 'out.txt'
    scale = 0.43
    cols = 80
    print('generating ASCII art...')
    aimg = covertImageToAscii(imgFile, cols, scale, moreLevels=100)

    # open a new text file
    f = open(outFile, 'w')
    # write each string in the list to the new file
    for row in aimg:
        f.write(row + '\n')
    # clean up
    f.close()
    print("ASCII art written to %s" % outFile)

if __name__ == '__main__':
    main()