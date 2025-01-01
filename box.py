import pygame as pg
from load_image import load_image
from settings import *


class Box(pg.sprite.Sprite):
    # loading of image
    image = load_image("box.png")

    def __init__(self, sprites, pos):
        super().__init__(sprites)
        self.image = Box.image
        self.image = pg.transform.scale(self.image, (WIGHT_OF_BOX, HEIGHT_OF_BOX))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
