import pygame as pg
from system_files.screen_files.load_image import load_image
from system_files.settings import *
from system_files.screen_files.button import Button


def start_screen(screen, clock):
    # draw main fon
    fon = pg.transform.scale(load_image(('start_screen_images', 'background.jpg')), (WIGHT_OF_SCREEN, HEIGHT_OF_SCREEN))
    screen.blit(fon, (0, 0))
    wight, height = WIGHT_OF_SCREEN / 4, HEIGHT_OF_SCREEN / 8

    play = Button(load_image(('start_screen_images', 'play_btn.png')),
                  load_image(('start_screen_images', 'play_btn_act.png')), "play",
                  ((WIGHT_OF_SCREEN - wight) / 2, HEIGHT_OF_SCREEN / 4), wight, height)

    options = Button(load_image(('start_screen_images', 'options_btn.png')),
                     load_image(('start_screen_images', 'options_btn_act.png')), "options",
                     ((WIGHT_OF_SCREEN - wight) / 2, HEIGHT_OF_SCREEN / 4 + (height + 50)), wight, height)

    exit_ = Button(load_image(('start_screen_images', 'exit_btn.png')),
                   load_image(('start_screen_images', 'exit_btn_act.png')), "exit",
                   ((WIGHT_OF_SCREEN - wight) / 2, HEIGHT_OF_SCREEN / 4 + 2 * (height + 50)), wight, height)

    while True:
        screen.blit(fon, (0, 0))
        for event in pg.event.get():
            if (a := play.check_event(event)) is not None:
                return a
            if (a := options.check_event(event)) is not None:
                return a
            if (a := exit_.check_event(event)) is not None:
                return a
        play.draw(screen)
        options.draw(screen)
        exit_.draw(screen)
        pg.display.flip()
        clock.tick(FPS)
