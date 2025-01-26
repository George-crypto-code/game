import pygame as pg
import pygame_widgets as pg_wd
from pygame_widgets.slider import Slider
from system_files.screen_files.load_image import load_image
from system_files.screen_files.button import Button
from system_files.settings import *


def options_screen(screen, clock):
    # draw main fon
    fon = pg.transform.scale(load_image(("options_screen_images", "options_board.png")),
                             (WIGHT_OF_SCREEN, HEIGHT_OF_SCREEN))
    screen.blit(fon, (0, 0))
    # cords for home btn
    size_btn = WIGHT_OF_SCREEN / 10, WIGHT_OF_SCREEN / 10
    # draw home btn
    home_btn = Button(load_image(('victory_screen_images', 'home_btn.png')),
                      load_image(('victory_screen_images', 'home_btn_act.png')), "home",
                      ((WIGHT_OF_SCREEN - size_btn[0]) / 2, HEIGHT_OF_SCREEN / 4 * 3), *size_btn)
    # slider x cord and flag for moving
    with open(r"system_files\sound_effect_loud.txt") as loud:
        loud_of_game = float(loud.readline())
    sound_btn_on = Button(load_image(("options_screen_images", "sound.png")),
                          load_image(("options_screen_images", "sound_act.png")), "off",
                          (WIGHT_OF_SCREEN / 20 * 2, HEIGHT_OF_SCREEN / 20 * 11), *size_btn)

    sound_btn_off = Button(load_image(("options_screen_images", "sound_offed.png")),
                           load_image(("options_screen_images", "sound_offed_act.png")), "on",
                           (WIGHT_OF_SCREEN / 20 * 2, HEIGHT_OF_SCREEN / 20 * 11), *size_btn)

    curr_sound_btn = sound_btn_on if loud_of_game else sound_btn_off

    left_slider, top_slider = int(WIGHT_OF_SCREEN / 20 * 5), int(HEIGHT_OF_SCREEN / 20 * 12)
    size_slider = int(WIGHT_OF_SCREEN / 10 * 6), int(HEIGHT_OF_SCREEN / 20 * 1)
    slider = Slider(screen, left_slider, top_slider, size_slider[0], size_slider[1], min=0, max=1, step=0.1)
    slider.setValue(loud_of_game)

    while True:
        screen.blit(fon, (0, 0))
        events = pg.event.get()
        for event in events:
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                return None

            if slider.getValue() == 0:
                curr_sound_btn = sound_btn_off
            else:
                curr_sound_btn = sound_btn_on

            if (a := home_btn.check_event(event)) is not None:
                return a

            if (a := curr_sound_btn.check_event(event)) is not None:
                loud_of_game = 0 if loud_of_game else 0.5
                slider.setValue(loud_of_game)
                if a == "on":
                    curr_sound_btn = sound_btn_on
                else:
                    curr_sound_btn = sound_btn_off

        with open(r"system_files\sound_effect_loud.txt", mode="w") as loud:
            loud.write(str(slider.getValue()))
        curr_sound_btn.draw(screen)
        home_btn.draw(screen)
        pg_wd.update(events)
        pg.display.flip()
        clock.tick(FPS)
