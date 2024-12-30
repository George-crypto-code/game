import pygame as pg
import math
from settings import *
from load_image import load_image


class Player(pg.sprite.Sprite):
    image = load_image("player.png")

    def __init__(self, sprites):
        super().__init__(sprites)
        self.image = Player.image
        self.image = pg.transform.scale(self.image, (WIGHT_OF_PLAYER, HEIGHT_OF_PLAYER))
        self.orig_img = self.image.copy()
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.rect.x = 0
        self.rect.y = 0
        self.player_angle = PLAYER_ANGLE

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

    def change_angle(self, pos):
        self.player_angle = (180 / math.pi) * -math.atan((pos[1] - self.rect.y) / (pos[0] - self.rect.x))
        self.image = pg.transform.rotate(self.orig_img, int(self.player_angle))
        self.rect = self.image.get_rect(center=(self.rect.x, self.rect.y))

        # mouse_x, mouse_y = pygame.mouse.get_pos()
        # angle = (180 / math.pi) * -math.atan2(mouse_y - self.y, mouse_x - self.x)
        # self.image = pygame.transform.rotate(self.original_image, int(angle))
        # self.rect = self.image.get_rect(center=self.position)

        # _, angle = (pg.mouse.get_pos() - self.pos).as_polar()
        # self.image = pg.transform.rotozoom(self.orig_img, -angle, 1)
        # self.rect = self.image.get_rect(center=self.rect.center)
