#!/usr/bin/env python3

from PIL import Image


def main():

    image = Image.open('pixelcat.png')

    image_flip = flip_horizontal(image)
    image_flip.show()

    grey_img = grey(image)
    grey_img.show()

    image_blur = blur(image)
    image_blur.show()


def grey(image):

    grey_img = image.copy()
    pixels = grey_img.load()

    for x in range(image.size[0]):
        for y in range(image.size[1]):

            (r, g, b,) = pixels[x, y]
            grey = int(0.299 * r + 0.587 * g + 0.114 * b)
            pixels[x, y] = (grey, grey, grey)

    return grey_img


def blur(image):

    width = image.size[0]
    height = image.size[1]

    blur_img = Image.new(mode="RGB", size=(width, height))
    pixels_origin = image.load()
    pixels_result = blur_img.load()

    for x in range(width):
        for y in range(height):

            r = blur_pix_channel(pixels_origin, x, y, 0, width, height)
            g = blur_pix_channel(pixels_origin, x, y, 1, width, height)
            b = blur_pix_channel(pixels_origin, x, y, 2, width, height)

            pixels_result[x, y] = (r, g, b,)

    return blur_img

def blur_pix_channel(pixels, x, y, channel, w, h):

    value = get_pixel(pixels, x, y, channel, w, h) * 4

    value += get_pixel(pixels, x, y-1, channel, w, h) * 2
    value += get_pixel(pixels, x, y+1, channel, w, h) * 2
    value += get_pixel(pixels, x+1, y, channel, w, h) * 2
    value += get_pixel(pixels, x-1, y, channel, w, h) * 2

    value += get_pixel(pixels, x-1, y-1, channel, w, h)
    value += get_pixel(pixels, x-1, y+1, channel, w, h)
    value += get_pixel(pixels, x+1, y-1, channel, w, h)
    value += get_pixel(pixels, x+1, y+1, channel, w, h)

    return int(value / 16)


def get_pixel(pixels, x, y, channel, w, h):

    if x < 0:
        x = 0
    if y < 0:
        y = 0
    if x >= w:
        x = w - 1
    if y >= h:
        y = h - 1

    return pixels[x, y][channel]

def flip_horizontal(image):

    flip_img = image.copy()
    pixels = flip_img.load()

    (w, h,) = image.size
    
    for x in range(int(w / 2)):
        for y in range(h):

            save_pixel = pixels[x, y]
            pixels[x, y] = pixels[w - 1 - x, y]
            pixels[w - 1 - x, y] = save_pixel
            
    return flip_img

if __name__ == "__main__":
    main()
