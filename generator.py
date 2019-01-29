import os
from PIL import Image, ImageDraw, ImageFont, ImageChops
import csv

def trim(im):
    bg = Image.new(im.mode, im.size, (255, 0, 0, 0))
    diff = ImageChops.difference(im, bg)
    bbox = diff.getbbox()
    if bbox:
        #newbbox = (bbox[0] - 50, bbox[1], bbox[2] + 50, bbox[3])
        #return im.crop(newbbox)
        return im.crop(bbox)
    else:
        # found no content
        raise ValueError("cannot trim; image was empty")

#font = ImageFont.truetype('./fonts/montserrat/Montserrat-Medium.otf', size=600)
font = ImageFont.truetype('./fonts/metropolis/Metropolis-Bold.otf', size=600)
(x, y) = (0, 0) # x = 22 for the I in Roboto Mono font
color = 'rgb(255, 255, 255)' # white color
dotcolor = 'rgb(74,224,149)'

image = Image.new('RGBA', (10000, 10000), (255, 0, 0, 0))
draw = ImageDraw.Draw(image)
message1 = 'Puppet'
message2 = '.'

draw.text((x, y), message1, fill=color, font=font)
width = font.getsize(message1)[0]
draw.text((width, y), message2, fill=dotcolor, font=font)

image = trim(image)
image.save('./logo.png')