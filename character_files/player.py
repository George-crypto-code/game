import pygame as pg
import math
from system_files.settings import *
from system_files.load_image import load_image


# class for main player
class Player(pg.sprite.Sprite):
    # loading of image
    image = load_image(r"level_screen_images\player.png")

    def __init__(self, sprites, screen, pos):
        super().__init__(sprites)
        self.image = Player.image
        # scale for image because image is very big
        self.image = pg.transform.scale(self.image, (WIGHT_OF_PLAYER, HEIGHT_OF_PLAYER))
        # copy image for rotate
        self.orig_img = self.image.copy()
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.rect.x, self.rect.y = pos
        self.player_angle = PLAYER_ANGLE
        self.screen = screen
        # player health
        self.player_health = PLAYER_MAX_HEALTH

    # method for movement player
    def movement(self, all_borders, all_boxes):
        keys = pg.key.get_pressed()
        horizontal_top_borders, horizontal_bot_borders, vertical_left_borders, vertical_right_borders = all_borders
        if keys[pg.K_d]:
            self.rect.x += PLAYER_SPEED
            # check on touch borders or boxes
            if (pg.sprite.collide_mask(self, vertical_right_borders) or
                    any(pg.sprite.collide_mask(self, elem) for elem in all_boxes)):
                self.rect.x -= PLAYER_SPEED

        if keys[pg.K_a]:
            self.rect.x -= PLAYER_SPEED
            # check on touch borders or boxes
            if (pg.sprite.collide_mask(self, vertical_left_borders) or
                    any(pg.sprite.collide_mask(self, elem) for elem in all_boxes)):
                self.rect.x += PLAYER_SPEED

        if keys[pg.K_w]:
            self.rect.y -= PLAYER_SPEED
            # check on touch borders or boxes
            if (pg.sprite.collide_mask(self, horizontal_top_borders) or
                    any(pg.sprite.collide_mask(self, elem) for elem in all_boxes)):
                self.rect.y += PLAYER_SPEED

        if keys[pg.K_s]:
            self.rect.y += PLAYER_SPEED
            # check on touch borders or boxes
            if (pg.sprite.collide_mask(self, horizontal_bot_borders) or
                    any(pg.sprite.collide_mask(self, elem) for elem in all_boxes)):
                self.rect.y -= PLAYER_SPEED

    # rotate on mouse cursor
    def change_angle(self, pos):
        x, y = self.rect.center
        self.player_angle = -math.degrees(math.atan2((pos[1] - y), (pos[0] - x)))
        self.image = pg.transform.rotate(self.orig_img, self.player_angle)
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=self.rect.center)

    # method for check hit-and-miss to box
    def shoot(self, pos, enemy, all_boxes):
        x, y = pos
        x += WIGHT_OF_AIM // 2
        y += HEIGHT_OF_AIM // 2
        i, j = self.rect.center
        # hit or not
        if all(False if box.rect.clipline((x, y), (i, j)) else True for box in all_boxes):
            enemy[0].enemy_health -= 1
            return True
        return False

    def check_health(self):
        # check player health
        # if health 0 than player die
        if self.player_health <= 0:
            self.kill()
