import pygame as pg
from system_files.screen_files.load_image import load_image
from system_files.settings import *


def options_screen(screen, clock):
    # draw main fon
    fon = pg.transform.scale(load_image(("options_screen_images", "options_board.png")),
                             (WIGHT_OF_SCREEN, HEIGHT_OF_SCREEN))
    screen.blit(fon, (0, 0))
    # cords for home btn
    left_home, top_home = WIGHT_OF_SCREEN // 2 - 50, HEIGHT_OF_SCREEN - 105
    # draw home btn
    home_btn = pg.transform.scale(load_image(("options_screen_images", "home_btn.png")), (100, 100))
    screen.blit(home_btn, (left_home, top_home))
    # slider x cord and flag for moving
    with open(r"system_files\sound_effect_loud.txt") as loud:
        loud_of_game = float(loud.readline())
    slider_x = 240 + loud_of_game * 400
    moving = False

    # cords for sound effect btn
    left_sound, top_sound = 100, 250
    name_of_sound = "sound_offed" if slider_x <= 243 else "sound"
    # draw sound effect btn
    sound = pg.transform.scale(load_image(("options_screen_images", name_of_sound + ".png")), (100, 100))
    screen.blit(sound, (left_sound, top_sound))

    while True:
        screen.blit(fon, (0, 0))
        screen.blit(home_btn, (left_home, top_home))
        screen.blit(sound, (left_sound, top_sound))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

            if event.type == pg.MOUSEMOTION:
                x, y = event.pos
                # when cursor on btn than it lights
                if left_home <= x <= left_home + 100 and top_home <= y <= top_home + 100:
                    home_btn = pg.transform.scale(load_image(('options_screen_images', 'home_btn_act.png')), (100, 100))
                else:
                    home_btn = pg.transform.scale(load_image(('options_screen_images', 'home_btn.png')), (100, 100))
                # when cursor on btn than it lights
                if left_sound <= x <= left_sound + 100 and top_sound <= y <= top_sound + 100:
                    sound = pg.transform.scale(load_image(('options_screen_images', name_of_sound + "_act.png")),
                                               (100, 100))
                else:
                    sound = pg.transform.scale(load_image(('options_screen_images', name_of_sound + ".png")),
                                               (100, 100))
                # if flag than slider start moving
                if moving and 240 <= slider_x + event.rel[0] <= 640:
                    slider_x += event.rel[0]
                    name_of_sound = "sound_offed" if slider_x <= 243 else "sound"
                else:
                    moving = False

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                # if user clicked on home btn than it return to start window
                if left_home < x < left_home + 100 and top_home < y < top_home + 100:
                    return "home"
                # if user clicked on slider than flag change
                if slider_x < event.pos[0] < slider_x + 20 and 275 < event.pos[1] < 325:
                    moving = True
                # if user clicked on sound effect btn than it change on offed sound
                if left_sound < x < left_sound + 100 and top_sound < y < top_sound + 100:
                    if slider_x > 240:
                        slider_x = 240
                        name_of_sound = "sound_offed"
                    else:
                        slider_x = 360
                        name_of_sound = "sound"

                    sound = pg.transform.scale(load_image(('options_screen_images', name_of_sound + "_act.png")),
                                               (100, 100))
            # if user stop holding mouse than flag change
            if event.type == pg.MOUSEBUTTONUP:
                moving = False

            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                return None
        if slider_x != 250 + loud_of_game * 400:
            with open(r"system_files\sound_effect_loud.txt", mode="w") as loud:
                loud.write(str((slider_x - 240) / 400))
        # draw rect for sound effects
        pg.draw.rect(screen, "black", (250, 300, 400, 5))
        pg.draw.rect(screen, "grey", (slider_x, 275, 20, 50))
        pg.display.flip()
        clock.tick(FPS)
