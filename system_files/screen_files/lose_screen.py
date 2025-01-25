import pygame as pg
from system_files.screen_files.load_image import load_image
from system_files.screen_files.button import Button
from system_files.settings import *


def lose_screen(screen, clock):
    # draw main fon
    fon = pg.transform.scale(load_image(('lose_screen_images', 'game_over.jpg')), (WIGHT_OF_SCREEN, HEIGHT_OF_SCREEN))
    screen.blit(fon, (0, 0))
    size = WIGHT_OF_SCREEN / 8, WIGHT_OF_SCREEN / 8
    left, top = (WIGHT_OF_SCREEN - size[0]) / 2, HEIGHT_OF_SCREEN / 5 * 4
    restart_btn = Button(load_image(('lose_screen_images', 'restart.png')),
                         load_image(('lose_screen_images', 'restart_act.png')), "restart", (left, top), *size)

    while True:
        for event in pg.event.get():
            if (a := restart_btn.check_event(event)) is not None:
                return a
        restart_btn.draw(screen)
        pg.display.flip()
        clock.tick(FPS)
