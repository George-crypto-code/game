import pygame as pg
from system_files.screen_files.load_image import load_image
from system_files.settings import *


def options_screen(screen, clock, loud_of_game):
    # draw main fon
    fon = pg.transform.scale(load_image(('options_screen_images', 'options_board.png')),
                             (WIGHT_OF_SCREEN, HEIGHT_OF_SCREEN))
    screen.blit(fon, (0, 0))

    left_home, top_home = WIGHT_OF_SCREEN // 2 - 50, HEIGHT_OF_SCREEN - 105
    home_btn = pg.transform.scale(load_image(('options_screen_images', 'home_btn.png')), (100, 100))
    screen.blit(home_btn, (left_home, top_home))

    left_sound, top_sound = 100, 250
    name_of_sound = 'sound'
    sound_flag = True
    sound = pg.transform.scale(load_image(('options_screen_images', name_of_sound + ".png")), (100, 100))
    screen.blit(sound, (left_sound, top_sound))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

            if event.type == pg.MOUSEMOTION:
                x, y = event.pos
                if left_home <= x <= left_home + 100 and top_home <= y <= top_home + 100:
                    home_btn = pg.transform.scale(load_image(('options_screen_images', 'home_btn_act.png')), (100, 100))
                else:
                    home_btn = pg.transform.scale(load_image(('options_screen_images', 'home_btn.png')), (100, 100))
                screen.blit(home_btn, (left_home, top_home))

                if left_sound <= x <= left_sound + 100 and top_sound <= y <= top_sound + 100:
                    sound = pg.transform.scale(load_image(('options_screen_images', name_of_sound + "_act.png")), (100, 100))
                else:
                    sound = pg.transform.scale(load_image(('options_screen_images', name_of_sound + ".png")), (100, 100))
                screen.blit(sound, (left_sound, top_sound))

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if left_home < x < left_home + 100 and top_home < y < top_home + 100:
                    return 1

                if left_sound < x < left_sound + 100 and top_sound < y < top_sound + 100:
                    if sound_flag:
                        name_of_sound = "sound_offed"
                        sound_flag = False
                    else:
                        name_of_sound = "sound"
                        sound_flag = True

                    sound = pg.transform.scale(load_image(('options_screen_images', name_of_sound + "_act.png")), (100, 100))
                    screen.blit(sound, (left_sound, top_sound))

            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                return None

        pg.display.flip()
        clock.tick(FPS)
