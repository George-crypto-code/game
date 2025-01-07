import pygame as pg
from system_files.settings import *
from system_files.start_screen import start_screen
from system_files.menu_screen import menu_screen
from levels.level_1 import All_sprites

pg.init()  # pygame initialization
clock = pg.time.Clock()  # clock for tick of game
screen = pg.display.set_mode((WIGHT_OF_SCREEN, HEIGHT_OF_SCREEN))  # game screen

start_screen(screen, clock)  # enter screen
while menu_screen(screen, clock):  # while player not choose the level menu not hide
    start_screen(screen, clock)  # if player choose the arrow back

all_sprites = pg.sprite.Group()  # all sprites for more readable code and it eazy to refix levels
a = All_sprites(all_sprites, screen)  # the chosen level
mouse_pos = (0, 0)

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
            if enemy := a.aim_image.check_shoot(a.enemy_sprites):  # if aim collide with enemy than raise shoot method
                a.player.shoot(event.pos, enemy, a.all_boxes)
    # main method in each level
    all_sprites.update(mouse_pos)  # it updates all sprites and draw them

    # system
    clock.tick(FPS)
    pg.display.flip()
