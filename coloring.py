#!/usr/bin/env python3

from PIL import Image

image = Image.open('volt.jpg')
pixels = image.load()

for x in range(image.size[0]):
    for y in range(image.size[1]):
        (r, g, b,) = pixels[x, y]

        grey = int(0.299 * r + 0.587 * g + 0.114 * b)

        pixels[x, y] = (grey, grey, grey)
image.show()
