import pygame as pg
import math
from system_files.settings import *
from system_files.load_image import load_image
from character_files.bullet import Bullet
from random import randrange


# class for enemy
class Enemy(pg.sprite.Sprite):
    # loading of image
    image = load_image("player.png")

    def __init__(self, sprites, pos):
        super().__init__(sprites)
        self.image = Enemy.image
        # scale for image because image is very big
        self.image = pg.transform.scale(self.image, (WIGHT_OF_ENEMY, HEIGHT_OF_ENEMY))
        self.orig_img = self.image.copy()
        self.image = pg.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.rect.x, self.rect.y = pos
        self.x, self.y = pos
        self.path = randrange(30, 50)
        self.enemy_speed = ENEMY_SPEED
        self.enemy_health = ENEMY_MAX_HEALTH
        self.enemy_angle = ENEMY_ANGLE
        self.movement_flag = True

    def update(self, player, all_boxes):
        if self.movement_flag:
            self.rect.y += self.enemy_speed
            if self.rect.y - self.y >= self.path or self.rect.y <= self.y:
                self.enemy_speed *= -1
                self.image = pg.transform.rotate(self.image, 180)

        if self.enemy_health <= 0:
            self.kill()
    "try to enemy shoot"

    #     a = Bullet((self.rect.x, self.rect.y), (player.rect.x, player.rect.y))
    #     flag = True
    #     for box in all_boxes:
    #         if pg.sprite.collide_mask(a, box):
    #             flag = False
    #             break
    #
    #     if flag:
    #         self.movement_flag = False
    #         self.change_angle(player)
    #     else:
    #         self.movement_flag = True
    #     a.kill()
    #
    # def change_angle(self, player):
    #     x, y = self.rect.center
    #     i, j = player.rect.center
    #     self.enemy_angle = -math.degrees(math.atan2((j - y), (i - x)))
    #     self.image = pg.transform.rotate(self.orig_img, self.enemy_angle)
    #     self.mask = pg.mask.from_surface(self.image)
    #     self.rect = self.image.get_rect(center=self.rect.center)
