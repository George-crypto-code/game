import pygame as pg
from system_files.load_image import load_image
from system_files.settings import *


class Map(pg.sprite.Sprite):
    # loading of image
    image = load_image(("level_screen_images", "field.png"))

    def __init__(self, sprites):
        super().__init__(sprites)
        self.image = Map.image
        self.image = pg.transform.scale(self.image, (WIGHT_OF_MAP, HEIGHT_OF_MAP))
        self.rect = self.image.get_rect()
