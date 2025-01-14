import pygame as pg
from system_files.load_image import load_image
from system_files.settings import *


def menu_screen(screen, clock):
    left, top = 150, 150
    # draw main fon
    fon = pg.transform.scale(load_image(r'menu_screen_images\background.jpg'), (WIGHT_OF_SCREEN, HEIGHT_OF_SCREEN))
    screen.blit(fon, (0, 0))

    level_1 = load_image(r'menu_screen_images\level_1.png')
    screen.blit(level_1, (left, top))

    arrow = load_image(r'menu_screen_images\arrow.png')
    screen.blit(arrow, (10, 10))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

            if event.type == pg.MOUSEMOTION:
                x, y = event.pos
                if left < x < left + 100 and top < y < top + 100:
                    level_1 = load_image(r'menu_screen_images\level_1_act.png')
                else:
                    level_1 = load_image(r'menu_screen_images\level_1.png')
                screen.blit(level_1, (left, top))

                if 10 < x < 86 and 10 < y < 86:
                    arrow = load_image(r'menu_screen_images\arrow_act.png')
                else:
                    arrow = load_image(r'menu_screen_images\arrow.png')
                screen.blit(arrow, (10, 10))

            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos
                if left < x < left + 100 and top < y < top + 100:
                    return 1
                if 10 < x < 86 and 10 < y < 86:
                    return 0
            pg.draw.rect(screen, "black", (100, 100, 600, 400), 3)

        pg.display.flip()
        clock.tick(FPS)
