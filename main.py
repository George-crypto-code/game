import pygame as pg
from system_files.settings import *
from character_files.player import Player
from character_files.enemy import Enemy
from map_loader_files.world_map import Map
from map_loader_files.border import Border
from map_loader_files.box import Box
from map_loader_files.aim import Aim
from system_files.start_screen import start_screen
from system_files.menu_screen import menu_screen

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((WIGHT_OF_SCREEN, HEIGHT_OF_SCREEN))

start_screen(screen, clock)
menu_screen(screen, clock)

# set player
player_sprites = pg.sprite.Group()
player = Player(player_sprites, screen, (0, 0))
# set enemies
enemy_sprites = pg.sprite.Group()
Enemy(enemy_sprites, (600, 300))
Enemy(enemy_sprites, (320, 200))
Enemy(enemy_sprites, (350, 350))
Enemy(enemy_sprites, (520, 80))
Enemy(enemy_sprites, (250, 400))
# set boxes
all_boxes = pg.sprite.Group()
Box(all_boxes, (100, 50))
Box(all_boxes, (450, 100))
Box(all_boxes, (540, 540))
Box(all_boxes, (250, 200))
# set borders
all_borders = pg.sprite.Group()
horizontal_top_borders = Border(all_borders, 0, 0, WIGHT_OF_MAP - 1, 0)
horizontal_bot_borders = Border(all_borders, 0, HEIGHT_OF_MAP - 1, WIGHT_OF_MAP - 1, HEIGHT_OF_MAP - 1)
vertical_left_borders = Border(all_borders, 0, 0, 0, HEIGHT_OF_MAP - 1)
vertical_right_borders = Border(all_borders, WIGHT_OF_MAP - 1, 0, WIGHT_OF_MAP - 1, HEIGHT_OF_MAP - 1)
# set map
map_sprites = pg.sprite.Group()
_ = Map(map_sprites)

mouse_pos = (0, 0)
# aim
aim_sprites = pg.sprite.Group()
aim_image = Aim(aim_sprites, mouse_pos)

# main gaming cycle
while True:
    screen.fill('black')
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.MOUSEMOTION:
            mouse_pos = event.pos
            pg.mouse.set_visible(False)
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if enemy := aim_image.check_shoot(enemy_sprites):  # if aim collide with enemy than raise shoot method
                player.shoot(event.pos, enemy, all_boxes)
    # draw aim
    aim_sprites.update(mouse_pos)
    # update player
    player.change_angle(mouse_pos)
    # check player and borders
    player.movement((horizontal_top_borders, horizontal_bot_borders, vertical_left_borders, vertical_right_borders),
                    all_boxes)
    # update enemies
    enemy_sprites.update(player, all_boxes)

    # drawing all things
    map_sprites.draw(screen)
    player_sprites.draw(screen)
    enemy_sprites.draw(screen)
    all_borders.draw(screen)
    all_boxes.draw(screen)
    aim_sprites.draw(screen)

    pg.draw.line(screen, "red", player.rect.center,
                 (mouse_pos[0] + WIGHT_OF_AIM // 2, mouse_pos[1] + HEIGHT_OF_AIM // 2))

    # system
    clock.tick(FPS)
    pg.display.flip()
