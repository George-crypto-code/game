import pygame as pg
from system_files.load_image import load_image
from system_files.settings import *


class Box(pg.sprite.Sprite):
    # loading of image
    image = load_image(("level_screen_images", "box.png"))

    def __init__(self, sprites, pos):
        super().__init__(sprites)
        self.image = Box.image
        self.image = pg.transform.scale(self.image, (WIGHT_OF_BOX, HEIGHT_OF_BOX))
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.rect.x, self.rect.y = pos
