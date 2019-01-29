import os
from PIL import Image, ImageDraw, ImageFont, ImageChops
import csv


#font = ImageFont.truetype('./fonts/montserrat/Montserrat-Medium.otf', size=600)
font = ImageFont.truetype('./fonts/metropolis/Metropolis-Bold.otf', size=600)
(x, y) = (0, -100) # x = 22 for the I in Roboto Mono font
color = 'rgb(255, 255, 255)' # white color
dotcolor = 'rgb(74,224,149)'

image = Image.new('RGBA', (10000, 10000), (74,224,149))
draw = ImageDraw.Draw(image)
message1 = 'p'

draw.text((x, y), message1, fill=color, font=font)
width, height = font.getsize(message1)

image = image.crop((0, 0, width, height - 30))

image.save('./favicon1.png')