import pygame as pg
from system_files.load_image import load_image
from system_files.settings import *


def options_screen(screen, clock):
    # draw main fon
    fon = pg.transform.scale(load_image(r'options_screen_images\options_board.png'),
                             (WIGHT_OF_SCREEN, HEIGHT_OF_SCREEN))
    screen.blit(fon, (0, 0))

    left, top = WIGHT_OF_SCREEN // 2 - 50, HEIGHT_OF_SCREEN - 105
    home_btn = pg.transform.scale(load_image(r'options_screen_images\home_btn.png'), (100, 100))
    screen.blit(home_btn, (left, top))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

            if event.type == pg.MOUSEMOTION:
                x, y = event.pos
                if left <= x <= left + 100 and top <= y <= top + 100:
                    home_btn = pg.transform.scale(load_image(r'options_screen_images\home_btn_act.png'), (100, 100))
                else:
                    home_btn = pg.transform.scale(load_image(r'options_screen_images\home_btn.png'), (100, 100))
                screen.blit(home_btn, (left, top))

            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos
                if left < x < left + 100 and top < y < top + 100:
                    return 1
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                return None

        pg.display.flip()
        clock.tick(FPS)
