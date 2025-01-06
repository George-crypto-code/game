import pygame as pg
from system_files.load_image import load_image
from system_files.settings import *


class Aim(pg.sprite.Sprite):
    # loading of image
    image = load_image("aim.png")

    def __init__(self, sprites, pos):
        super().__init__(sprites)
        self.image = Aim.image
        self.image = pg.transform.scale(self.image, (WIGHT_OF_AIM, HEIGHT_OF_AIM))
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.rect.x, self.rect.y = pos

    def check_shoot(self, enemies):
        return pg.sprite.spritecollide(self, enemies, False)

    def update(self, pos):
        self.rect.x, self.rect.y = pos
