import math
import pygame as pg
from settings import *


class Bullet(pg.sprite.Sprite):
    def __init__(self, player_pos, enemy_pos, all_sprites):
        super().__init__(all_sprites)
        # cords for drawing line
        player_x, player_y = player_pos
        enemy_x, enemy_y = enemy_pos
        line_length = math.hypot(player_x - enemy_x, player_y - enemy_y)
        angle = -math.degrees(math.atan2((enemy_y - player_y), (enemy_x - player_x)))
        self.image = pg.Surface((line_length, 1))
        self.image = pg.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.rect.x, self.rect.y = player_x + WIGHT_OF_PLAYER // 2, player_y + HEIGHT_OF_PLAYER // 2
        self.image.fill("black")
