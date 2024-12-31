import pygame as pg
from load_image import load_image
from settings import *


class Map(pg.sprite.Sprite):
    # loading of image
    image = load_image("field.png")

    def __init__(self, sprites):
        super().__init__(sprites)
        self.image = Map.image
        self.image = pg.transform.scale(self.image, (WIGHT_OF_MAP, HEIGHT_OF_MAP))
        self.rect = self.image.get_rect()
