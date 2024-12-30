import pygame as pg
import math
from settings import *
from load_image import load_image

# class for main player
class Player(pg.sprite.Sprite):
    # loading of image
    image = load_image("player.png")

    def __init__(self, sprites):
        super().__init__(sprites)
        self.image = Player.image
        # scale for image because image is very big
        self.image = pg.transform.scale(self.image, (WIGHT_OF_PLAYER, HEIGHT_OF_PLAYER))
        # copy image for rotate
        self.orig_img = self.image.copy()
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.rect.x = 0
        self.rect.y = 0
        self.player_angle = PLAYER_ANGLE

    # method for movement player
    def movement(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_d]:
            self.rect.x += PLAYER_SPEED
        if keys[pg.K_a]:
            self.rect.x -= PLAYER_SPEED
        if keys[pg.K_w]:
            self.rect.y -= PLAYER_SPEED
        if keys[pg.K_s]:
            self.rect.y += PLAYER_SPEED

    # rotate on mouse cursor
    def change_angle(self, pos):
        x, y = self.rect.x, self.rect.y
        self.player_angle = -math.degrees(math.atan2((pos[1] - y), (pos[0] - x)))
        self.image = pg.transform.rotate(self.orig_img, self.player_angle)
        self.rect = self.image.get_rect(center=self.rect.center)
