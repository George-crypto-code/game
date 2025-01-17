import os
import sys
import pygame as pg

# need initialization and set_mode because there will be mistake
pg.init()
pg.display.set_mode((500, 500))

# function for loading image
def load_image(names, color_key=None):
    fullname = os.path.join('data', 'images', *names)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pg.image.load(fullname)
    if color_key is not None:
        image = image.convert()
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image
