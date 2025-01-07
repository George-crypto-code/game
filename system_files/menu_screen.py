import pygame as pg
from system_files.load_image import load_image
from system_files.settings import *


def menu_screen(screen, clock):
    # draw main fon
    fon = pg.transform.scale(load_image(r'menu_screen_images\background.jpg'), (WIGHT_OF_SCREEN, HEIGHT_OF_SCREEN))
    screen.blit(fon, (0, 0))

    level_1 = load_image(r'menu_screen_images\level_1.png')
    screen.blit(level_1, (100, 100))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

            if event.type == pg.MOUSEMOTION:
                x, y = event.pos
                if 100 < x < 100 + 100 and 100 < y < 100 + 100:
                    level_1 = load_image(r'menu_screen_images\level_1_act.png')
                else:
                    level_1 = load_image(r'menu_screen_images\level_1.png')
                screen.blit(level_1, (100, 100))

            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 100 < x < 100 + 100 and 100 < y < 100 + 100:
                    return

        pg.display.flip()
        clock.tick(FPS)
