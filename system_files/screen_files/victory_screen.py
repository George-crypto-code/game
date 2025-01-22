import pygame as pg
from time import sleep
from system_files.screen_files.load_image import load_image
from system_files.settings import *


def victory_screen(screen, clock):
    sleep(1)
    shift = 0.05
    victory = pg.mixer.Sound(r'data/sounds/sound_effects/victory.wav')
    victory.set_volume(update_loud_of_game())
    victory.play()

    while shift < 1:
        shift += 0.05
        fon = pg.transform.scale(load_image(('victory_screen_images', 'victory_of_game.png')),
                                 (WIGHT_OF_SCREEN * shift, HEIGHT_OF_SCREEN * shift))
        screen.blit(fon, ((WIGHT_OF_SCREEN - WIGHT_OF_SCREEN * shift) // 2,
                          (HEIGHT_OF_SCREEN - HEIGHT_OF_SCREEN * shift) // 2))
        pg.display.flip()
        clock.tick(FPS)

    next_level = pg.transform.scale(load_image(('victory_screen_images', 'next_level.png')), (100, 100))
    screen.blit(next_level, (next_level_left := 450, next_level_top := 500))
    previous_level = pg.transform.scale(load_image(('victory_screen_images', 'previous_level.png')), (100, 100))
    screen.blit(previous_level, (previous_level_left := 250, previous_level_top := 500))
    home_btn = pg.transform.scale(load_image(('victory_screen_images', 'home_btn.png')), (100, 100))
    screen.blit(home_btn, (home_btn_left := 350, home_btn_top := 500))


    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.MOUSEMOTION:
                x, y = event.pos
                if previous_level_left <= x <= previous_level_left + 100 and previous_level_top <= y <= previous_level_top + 100:
                    previous_level = pg.transform.scale(load_image(('victory_screen_images', 'previous_level_act.png')), (100, 100))
                else:
                    previous_level = pg.transform.scale(load_image(('victory_screen_images', 'previous_level.png')), (100, 100))
                screen.blit(previous_level, (previous_level_left, previous_level_top))

                if next_level_left <= x <= next_level_left + 100 and next_level_top <= y <= next_level_top + 100:
                    next_level = pg.transform.scale(load_image(('victory_screen_images', 'next_level_act.png')), (100, 100))
                else:
                    next_level = pg.transform.scale(load_image(('victory_screen_images', 'next_level.png')), (100, 100))
                screen.blit(next_level, (next_level_left, next_level_top))

                if home_btn_left <= x <= home_btn_left + 100 and home_btn_top <= y <= home_btn_top + 100:
                    home_btn = pg.transform.scale(load_image(('victory_screen_images', 'home_btn_act.png')), (100, 100))
                else:
                    home_btn = pg.transform.scale(load_image(('victory_screen_images', 'home_btn.png')), (100, 100))
                screen.blit(home_btn, (home_btn_left, home_btn_top))

            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos
                if previous_level_left <= x <= previous_level_left + 100 and previous_level_top <= y <= previous_level_top + 100:
                    return -1
                if next_level_left <= x <= next_level_left + 100 and next_level_top <= y <= next_level_top + 100:
                    return 1
                if home_btn_left <= x <= home_btn_left + 100 and home_btn_top <= y <= home_btn_top + 100:
                    return "home"




        pg.display.flip()
        clock.tick(FPS)
