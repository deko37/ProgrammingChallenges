#!/usr/bin/python
# Programming challenge number 18 : Image to ASCII Art
from PIL import Image
import sys

if __name__ == "__main__":
    img = ""
    div_coef = 1
    if len(sys.argv) >= 2:
        img = sys.argv[1]
        div_coef = int(sys.argv[2])
    else:
        img = input("Where is the image you want to use (path with extension) ? ")
        div_coef = int(input("What division coef. you want to use ? "))
    img = Image.open(img).convert('L')
    red_wdth = img.width  / div_coef
    red_hgth = img.height / div_coef
    img.thumbnail((red_wdth, red_hgth))
    for y in range(img.height):
        for x in range(img.width):
            px_color = img.getpixel((x, y))
            if px_color > 250:
                print('@' * 2, end='')
            elif px_color > 180:
                print('#' * 2, end='')
            elif px_color > 125:
                print(':' * 2, end='')
            elif px_color > 90:
                print(',' * 2, end='')
            elif px_color > 45:
                print('.' * 2, end='')
            else:
                print(' ' * 2, end='')
        print()
