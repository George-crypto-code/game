import pygame as pg
from time import sleep
from system_files.screen_files.load_image import load_image
from system_files.screen_files.button import Button
from system_files.settings import *


def victory_screen(screen, clock, level):
    sleep(1)
    shift = 0.05
    victory = pg.mixer.Sound(r'data/sounds/sound_effects/victory.wav')
    victory.set_volume(update_loud_of_game()[0])
    victory.play()

    while shift < 1:
        shift += 0.05
        fon = pg.transform.scale(load_image(('victory_screen_images', 'victory_of_game.png')),
                                 (WIGHT_OF_SCREEN * shift, HEIGHT_OF_SCREEN * shift))
        screen.blit(fon, ((WIGHT_OF_SCREEN - WIGHT_OF_SCREEN * shift) // 2,
                          (HEIGHT_OF_SCREEN - HEIGHT_OF_SCREEN * shift) // 2))
        pg.display.flip()
        clock.tick(FPS)
    size = WIGHT_OF_SCREEN / 10, WIGHT_OF_SCREEN / 10
    next_level_flag, previous_level_flag = False, False
    if level < 3:
        next_level_flag = True
        next_level_left, next_level_top = WIGHT_OF_SCREEN / 10 * 6, HEIGHT_OF_SCREEN / 4 * 3
        next_level = Button(load_image(('victory_screen_images', 'next_level.png')),
                            load_image(('victory_screen_images', 'next_level_act.png')), 1,
                            (next_level_left, next_level_top), *size)

    if level > 1:
        previous_level_flag = True
        previous_level_left, previous_level_top = WIGHT_OF_SCREEN / 10 * 3, HEIGHT_OF_SCREEN / 4 * 3
        previous_level = Button(load_image(('victory_screen_images', 'previous_level.png')),
                                load_image(('victory_screen_images', 'previous_level_act.png')), 1,
                                (previous_level_left, previous_level_top), *size)

    home_btn = Button(load_image(('victory_screen_images', 'home_btn.png')),
                      load_image(('victory_screen_images', 'home_btn_act.png')), "home",
                      ((WIGHT_OF_SCREEN - size[0]) / 2, HEIGHT_OF_SCREEN / 4 * 3), *size)

    while True:
        screen.blit(fon, (0, 0))
        for event in pg.event.get():
            if next_level_flag:
                if (a := next_level.check_event(event)) is not None:
                    return a
            if previous_level_flag:
                if (a := previous_level.check_event(event)) is not None:
                    return a
            if (a := home_btn.check_event(event)) is not None:
                return a
        if next_level_flag:
            next_level.draw(screen)
        if previous_level_flag:
            previous_level.draw(screen)
        home_btn.draw(screen)
        pg.display.flip()
        clock.tick(FPS)
