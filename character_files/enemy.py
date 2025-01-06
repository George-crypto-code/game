import pygame as pg
from system_files.settings import *
from system_files.load_image import load_image
from random import randrange


# class for enemy
class Enemy(pg.sprite.Sprite):
    # loading of image
    image = load_image("player.png")

    def __init__(self, sprites, pos):
        super().__init__(sprites)
        self.image = Enemy.image
        # scale for image because image is very big
        self.image = pg.transform.rotate(pg.transform.scale(self.image, (WIGHT_OF_ENEMY, HEIGHT_OF_ENEMY)), 270)
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.rect.x, self.rect.y = pos
        self.x, self.y = pos
        self.path = randrange(30, 50)
        self.enemy_speed = ENEMY_SPEED
        self.enemy_health = ENEMY_MAX_HEALTH

    def update(self):
        self.rect.y += self.enemy_speed
        if self.rect.y - self.y >= self.path or self.rect.y <= self.y:
            self.enemy_speed *= -1
            self.image = pg.transform.rotate(self.image, 180)

        if self.enemy_health <= 0:
            self.kill()

