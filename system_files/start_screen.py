import pygame as pg
from system_files.load_image import load_image
from system_files.settings import *


def start_screen(screen, clock):
    # draw main fon
    fon = pg.transform.scale(load_image(r'start_screen_images\background.jpg'), (WIGHT_OF_SCREEN, HEIGHT_OF_SCREEN))
    screen.blit(fon, (0, 0))
    # draw play button
    play = load_image(r'start_screen_images\play_btn.png')
    screen.blit(play, (229, 100))
    # draw options button
    options = load_image(r'start_screen_images\options_btn.png')
    screen.blit(options, (229, 220))
    # draw exit button
    exit_ = load_image(r'start_screen_images\exit_btn.png')
    screen.blit(exit_, (229, 340))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            # mouse cursor on button than button light
            if event.type == pg.MOUSEMOTION:
                x, y = event.pos
                if 229 < x < 229 + 343 and 100 < y < 100 + 91:
                    play = load_image(r'start_screen_images\play_btn_act.png')
                else:
                    play = load_image(r'start_screen_images\play_btn.png')
                screen.blit(play, (229, 100))

                if 229 < x < 229 + 343 and 220 < y < 220 + 91:
                    options = load_image(r'start_screen_images\options_btn_act.png')
                else:
                    options = load_image(r'start_screen_images\options_btn.png')
                screen.blit(options, (229, 220))

                if 229 < x < 229 + 343 and 340 < y < 340 + 91:
                    exit_ = load_image(r'start_screen_images\exit_btn_act.png')
                else:
                    exit_ = load_image(r'start_screen_images\exit_btn.png')
                screen.blit(exit_, (229, 340))

            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 229 < x < 229 + 343 and 100 < y < 100 + 91:
                    return

                if 229 < x < 229 + 343 and 220 < y < 220 + 91:
                    print(2)

                if 229 < x < 229 + 343 and 340 < y < 340 + 91:
                    exit()

        pg.display.flip()
        clock.tick(FPS)
