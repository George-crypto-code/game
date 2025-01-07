import math
import pygame as pg
from system_files.settings import *
from system_files.load_image import load_image

# this class need for check on not collide shoot with box
class Bullet(pg.sprite.Sprite):
    image = load_image(r"level_screen_images\bullet.png")

    def __init__(self, start_pos, finish_pos):
        super().__init__()
        # cords for drawing line
        start_x, start_y = start_pos
        finish_x, finish_y = finish_pos
        line_length = math.hypot(start_x - finish_x, start_y - finish_y)
        angle = -math.degrees(math.atan2((finish_y - start_y), (finish_x - start_x)))
        # set images and mask
        self.image = Bullet.image
        self.image = pg.transform.scale(self.image, (line_length, 1))
        self.image = pg.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.rect.x, self.rect.y = start_x + WIGHT_OF_PLAYER // 2, start_y + HEIGHT_OF_PLAYER // 2
