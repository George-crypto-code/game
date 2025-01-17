import pygame as pg
import math
from system_files.settings import *
from system_files.screen_files.load_image import load_image
from random import randrange


# class for enemy
class Enemy(pg.sprite.Sprite):
    # loading of image
    image = load_image(("level_screen_images", "player.png"))

    def __init__(self, sprites, pos):
        super().__init__(sprites)
        self.image = Enemy.image
        # scale for image because image is very big
        self.image = pg.transform.scale(self.image, (WIGHT_OF_ENEMY, HEIGHT_OF_ENEMY))
        self.orig_img = self.image.copy()  # image for correct rotate
        self.image = pg.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)
        self.rect.x, self.rect.y = pos
        self.path = pos[1], pos[1] + randrange(30, 50)  # length which enemy will go
        self.enemy_speed = ENEMY_SPEED
        self.enemy_health = ENEMY_MAX_HEALTH
        self.enemy_angle = ENEMY_ANGLE
        self.movement_flag, self.timer_flag = True, False
        self.MYEVENTTYPE = pg.USEREVENT + 1  # event for enemy shoot

    def update(self, player, all_boxes):
        if self.enemy_health <= 0:  # if enemy health zero
            self.kill()  # enemy die

        x, y = player.rect.center
        i, j = self.rect.center

        if all(False if box.rect.clipline((x, y), (i, j)) else True for box in all_boxes):
            self.movement_flag = False
            self.change_angle(player)
            shoot = pg.mixer.Sound(r'data/sounds/sound_effects/shoot.wav')
            shoot.set_volume(LOUD_OF_GAME)
            for event in pg.event.get():
                if event.type == self.MYEVENTTYPE:
                    print(1)
                    if player.player_health > 0:
                        shoot.play()
                        player.player_health -= 1

        if self.movement_flag:
            self.rect.y += self.enemy_speed
            if self.rect.y < self.path[0] or self.rect.y > self.path[1]:
                self.enemy_speed *= -1
                self.image = pg.transform.rotate(self.image, 180)

        if self.movement_flag and not self.timer_flag:
            self.timer_flag = True
            pg.time.set_timer(self.MYEVENTTYPE, 1000)

    def change_angle(self, player):  # when enemy see the player he watches on him
        x, y = self.rect.center
        i, j = player.rect.center
        self.enemy_angle = -math.degrees(math.atan2((j - y), (i - x)))
        self.image = pg.transform.rotate(self.orig_img, self.enemy_angle)
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=self.rect.center)
