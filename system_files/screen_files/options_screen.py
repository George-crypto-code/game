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
    with open(r"system_files\sound_loud.txt") as loud:
        sound_loud, music_loud = tuple(map(float, loud.readlines()))

    sound_btn_on = Button(load_image(("options_screen_images", "sound.png")),
                          load_image(("options_screen_images", "sound_act.png")), "off",
                          (WIGHT_OF_SCREEN / 20 * 2, HEIGHT_OF_SCREEN / 20 * 11), *size_btn)

    sound_btn_off = Button(load_image(("options_screen_images", "sound_offed.png")),
                           load_image(("options_screen_images", "sound_offed_act.png")), "on",
                           (WIGHT_OF_SCREEN / 20 * 2, HEIGHT_OF_SCREEN / 20 * 11), *size_btn)

    music_btn_on = Button(load_image(("options_screen_images", "music.png")),
                          load_image(("options_screen_images", "music_act.png")), "off",
                          (WIGHT_OF_SCREEN / 20 * 2, HEIGHT_OF_SCREEN / 20 * 7), *size_btn)

    music_btn_off = Button(load_image(("options_screen_images", "music_offed.png")),
                           load_image(("options_screen_images", "music_offed_act.png")), "on",
                           (WIGHT_OF_SCREEN / 20 * 2, HEIGHT_OF_SCREEN / 20 * 7), *size_btn)

    curr_sound_btn = sound_btn_on if sound_loud else sound_btn_off
    curr_music_btn = music_btn_on if sound_loud else music_btn_off

    sound_left_slider, sound_top_slider = int(WIGHT_OF_SCREEN / 20 * 5), int(HEIGHT_OF_SCREEN / 20 * 12)
    size_slider = int(WIGHT_OF_SCREEN / 10 * 6), int(HEIGHT_OF_SCREEN / 20 * 1)
    sound_slider = Slider(screen, sound_left_slider, sound_top_slider, size_slider[0],
                          size_slider[1], min=0, max=1, step=0.1)
    sound_slider.setValue(sound_loud)

    music_left_slider, music_top_slider = int(WIGHT_OF_SCREEN / 20 * 5), int(HEIGHT_OF_SCREEN / 20 * 8)
    music_slider = Slider(screen, music_left_slider, music_top_slider, size_slider[0],
                          size_slider[1], min=0, max=1, step=0.1)
    music_slider.setValue(music_loud)

    while True:
        screen.blit(fon, (0, 0))
        events = pg.event.get()
        for event in events:
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                return None

            if (a := home_btn.check_event(event)) is not None:
                return a

            if (a := curr_sound_btn.check_event(event)) is not None:
                sound_loud = 0 if sound_loud else 0.5
                sound_slider.setValue(sound_loud)
                if a == "on":
                    curr_sound_btn = sound_btn_on
                else:
                    curr_sound_btn = sound_btn_off

            if (a := curr_music_btn.check_event(event)) is not None:
                music_loud = 0 if music_loud else 0.5
                music_slider.setValue(music_loud)
                if a == "on":
                    curr_music_btn = music_btn_on
                else:
                    curr_music_btn = music_btn_off

        if sound_loud == 0:
            curr_sound_btn = sound_btn_off
        else:
            curr_sound_btn = sound_btn_on

        if music_loud == 0:
            curr_music_btn = music_btn_off
        else:
            curr_music_btn = music_btn_on

        with open(r"system_files\sound_loud.txt", mode="w") as loud:
            loud.write(str(sound_slider.getValue()) + "\n" + str(music_slider.getValue()))

        sound_loud = sound_slider.getValue()
        music_loud = music_slider.getValue()
        curr_sound_btn.draw(screen)
        curr_music_btn.draw(screen)
        home_btn.draw(screen)
        pg_wd.update(events)
        pg.display.flip()
        clock.tick(FPS)
