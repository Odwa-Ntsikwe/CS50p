import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()
args = ["-f", "--font"]

if len(sys.argv) < 2:
    font = random.choice(figlet.getFonts())
    figlet.setFont(fonts = font)
elif len(sys.argv) > 2 and sys.argv[1] in args and sys.argv[2] in fonts:
    figlet.setFont(font = sys.argv[2])
else:
    sys.exit("Invalid usage")

text = input("Input: ")

print("Output:", figlet.renderText(text))
