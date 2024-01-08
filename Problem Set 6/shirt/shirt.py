import sys
import os
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

extensions = [".jpg", ".jpeg", ".png"]
first_arg = os.path.splitext(sys.argv[1])
second_arg = os.path.splitext(sys.argv[2])

if first_arg[1] not in extensions or second_arg[1] not in extensions:
    sys.exit("Invalid input")
if first_arg[1] != second_arg[1]:
    sys.exit("Input and output have different extensions")

try:
    shirt = Image.open("shirt.png")
    with Image.open(sys.argv[1]) as im:
        size = shirt.size
        cropped_image = ImageOps.fit(im, size)
        cropped_image.paste(shirt, mask = shirt)
        cropped_image.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("Input does not exist")
