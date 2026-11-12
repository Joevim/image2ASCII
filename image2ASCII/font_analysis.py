from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont
import numpy as np
np.set_printoptions(threshold=np.inf)
font_path = r"C:\Users\Lim Hao\Downloads\IBM Font\IBMPlexMono-Regular.ttf"

def font_analysis(font_path):
    font = TTFont(r"C:\Users\Lim Hao\Downloads\IBM Font\IBMPlexMono-Regular.ttf")
    cmap = font.getBestCmap()
    characters = []
    comp_avg_darkness = []
    luminous_index = []
    for unicode_value in cmap:
        if 32 <= unicode_value <= 126:
            character = chr(unicode_value)
            characters.append(character)

    load_font = ImageFont.truetype(font_path, 48)

    for x in characters:
        image_text = Image.new("L",(64,64),255)
        draw = ImageDraw.Draw(image_text)
        left, top, right, bottom = draw.textbbox((0,0),x, font=load_font)
        width = right - left
        height = bottom - top
        x_pos = (64-width)//2 - left
        y_pos = (64-height)//2 - top

        draw.text((x_pos,y_pos),x,font = load_font, fill = 0)  
        pixels = np.array(image_text)
        darkness = (1-(pixels/255))
        avg_darkness = np.mean(1-(pixels/255))
        comp_avg_darkness.append(avg_darkness)


    char_darkness_tupled = list(zip(characters,comp_avg_darkness))
    sorted_cd_tupled = sorted(char_darkness_tupled,key=lambda pair:pair[1])

    min_darkness = sorted_cd_tupled[0][1]
    max_darkness = sorted_cd_tupled[-1][1]
    for character,darkness_temp in sorted_cd_tupled:
        conv_darkness = ((darkness_temp-min_darkness)/(max_darkness-min_darkness)) * 255
        luminous_index.append((character,conv_darkness))

    return luminous_index


