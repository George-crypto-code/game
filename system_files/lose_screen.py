import pygame as pg
from system_files.load_image import load_image
from system_files.settings import *


def lose_screen(screen, clock):
    # draw main fon
    fon = pg.transform.scale(load_image(r'lose_screen_images\game_over.jpg'), (WIGHT_OF_SCREEN, HEIGHT_OF_SCREEN))
    screen.blit(fon, (0, 0))

    restart_btn = pg.transform.scale(load_image(r'lose_screen_images\restart.png'), (150, 150))
    left, top = WIGHT_OF_SCREEN // 2 - 75, 450
    screen.blit(restart_btn, (left, top))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

            if event.type == pg.MOUSEMOTION:
                x, y = event.pos
                if left < x < left + 150 and top < y < top + 150:
                    restart_btn = pg.transform.scale(load_image(r'lose_screen_images\restart_act.png'), (150, 150))
                else:
                    restart_btn = pg.transform.scale(load_image(r'lose_screen_images\restart.png'), (150, 150))
                screen.blit(restart_btn, (left, top))

            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos
                if left < x < left + 150 and top < y < top + 150:
                    return

        pg.display.flip()
        clock.tick(FPS)
