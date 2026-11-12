import cv2
from pathlib import Path
import numpy as np

lum = [" ", ".", "-", "o", "=", "4", "H", "#"]

img_path = Path(input("Path of image file: ")).expanduser()
# img_path = "../test/test_images/felix.jpg"

img = cv2.imread(img_path)
img_gry = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

usr_res = 'O'
while usr_res != 'H' and usr_res != 'M' and usr_res != 'L':
    usr_res = input("Output resolution (H/M/L): ").upper()
    print(usr_res)

match usr_res:
    case 'H':
        img_gry_resized = cv2.resize(img_gry, None, fx=0.5, fy=0.5)
    case 'M':
        img_gry_resized = cv2.resize(img_gry, None, fx=0.25, fy=0.25)
    case 'L':
        img_gry_resized = cv2.resize(img_gry, None, fx=0.1, fy=0.1)

img_res = img_gry_resized.shape


# Find the character suitable for the luminance value
def find_char(lum_val):
    match lum_val:
        case lum_val if lum_val < 32:
            return lum[0]
        case lum_val if lum_val < 32*2:
            return lum[1]
        case lum_val if lum_val < 32*3:
            return lum[2]
        case lum_val if lum_val < 32*4:
            return lum[3]
        case lum_val if lum_val < 32*5:
            return lum[4]
        case lum_val if lum_val < 32*6:
            return lum[5]
        case lum_val if lum_val < 32*7:
            return lum[6]
        case lum_val if lum_val < 256:
            return lum[7]

for h in range(int(img_res[0]/2)):
    result_line = ""
    for w in range(img_res[1]):
        result_line += find_char(img_gry_resized[2*h, w])
    print(result_line)

