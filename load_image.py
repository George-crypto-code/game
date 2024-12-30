import os
import sys
import pygame as pg

# need initialization and set_mode because there will be mistake
pg.init()
pg.display.set_mode((500, 500))

# function for loading image
def load_image(name, colorkey=None):
    fullname = os.path.join('data', 'images',  name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pg.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image
