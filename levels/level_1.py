import pygame as pg
from system_files.settings import *
from character_files.player import Player
from character_files.enemy import Enemy
from map_loader_files.world_map import Map
from map_loader_files.border import Border
from map_loader_files.box import Box
from map_loader_files.aim import Aim


# class for each level
# very eazy to add new level
class AllSprites(pg.sprite.Sprite):
    def __init__(self, all_sprites, screen):
        super().__init__(all_sprites)
        self.screen = screen
        # set player
        self.player_sprites = pg.sprite.Group()
        self.player = Player(self.player_sprites, screen, (0, 0))
        # set enemies
        self.enemy_sprites = pg.sprite.Group()
        Enemy(self.enemy_sprites, (600, 300))
        Enemy(self.enemy_sprites, (320, 200))
        Enemy(self.enemy_sprites, (350, 350))
        Enemy(self.enemy_sprites, (520, 80))
        Enemy(self.enemy_sprites, (250, 400))
        # set boxes
        self.all_boxes = pg.sprite.Group()
        Box(self.all_boxes, (100, 50))
        Box(self.all_boxes, (450, 100))
        Box(self.all_boxes, (540, 540))
        Box(self.all_boxes, (250, 200))
        # set borders
        self.all_borders = pg.sprite.Group()
        self.horizontal_top_borders = Border(self.all_borders, 0, 0, WIGHT_OF_MAP - 1, 0)
        self.horizontal_bot_borders = Border(self.all_borders, 0, HEIGHT_OF_MAP - 1, WIGHT_OF_MAP - 1,
                                             HEIGHT_OF_MAP - 1)
        self.vertical_left_borders = Border(self.all_borders, 0, 0, 0, HEIGHT_OF_MAP - 1)
        self.vertical_right_borders = Border(self.all_borders, WIGHT_OF_MAP - 1, 0, WIGHT_OF_MAP - 1, HEIGHT_OF_MAP - 1)
        # set map
        self.map_sprites = pg.sprite.Group()
        Map(self.map_sprites)

        mouse_pos = (0, 0)
        # aim
        self.aim_sprites = pg.sprite.Group()
        self.aim_image = Aim(self.aim_sprites, mouse_pos)

    def update(self, mouse_pos):  # main method of all levels
        # draw aim
        self.aim_sprites.update(mouse_pos)
        # update player
        self.player.change_angle(mouse_pos)
        # check player and borders
        self.player.movement((self.horizontal_top_borders, self.horizontal_bot_borders, self.vertical_left_borders,
                              self.vertical_right_borders),
                             self.all_boxes)
        self.player.check_health()
        # update enemies
        self.enemy_sprites.update(self.player, self.all_boxes)

        # drawing all things
        self.map_sprites.draw(self.screen)
        self.player_sprites.draw(self.screen)
        self.enemy_sprites.draw(self.screen)
        self.all_borders.draw(self.screen)
        self.all_boxes.draw(self.screen)
        self.aim_sprites.draw(self.screen)
