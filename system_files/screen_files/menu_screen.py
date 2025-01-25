import pygame as pg
import csv
from system_files.screen_files.load_image import load_image
from system_files.screen_files.button import Button
from system_files.settings import *


def menu_screen(screen, clock):
    left_btn, top_btn = WIGHT_OF_SCREEN / 8, HEIGHT_OF_SCREEN / 8
    wight_btn, height_btn = WIGHT_OF_SCREEN / 10, WIGHT_OF_SCREEN / 10
    # draw main fon
    fon = pg.transform.scale(load_image(('menu_screen_images', 'background.jpg')), (WIGHT_OF_SCREEN, HEIGHT_OF_SCREEN))
    screen.blit(fon, (0, 0))

    with open(r"data\levels.csv", encoding="utf8") as csvfile:
        data_levels = tuple(csv.reader(csvfile, delimiter=';', quotechar='"'))

    levels = []
    for i in range(1, 4):
        level_path = "complete_levels" if data_levels[i][1] == "1" else "levels"
        level = Button(load_image(('menu_screen_images', level_path, f'level_{i}.png')),
                       load_image(('menu_screen_images', level_path, f'level_{i}_act.png')), i,
                       ((left_btn + 100) * i, top_btn), wight_btn, height_btn)
        levels.append(level)


    arrow = Button(load_image(('menu_screen_images', 'arrow.png')), load_image(('menu_screen_images', 'arrow_act.png')),
                   0, (WIGHT_OF_MAP / 100, HEIGHT_OF_SCREEN / 100), WIGHT_OF_SCREEN / 10, HEIGHT_OF_SCREEN / 10)

    while True:
        for event in pg.event.get():
            for level in levels:
                if (a := level.check_event(event)) is not None:
                    return a
            if (a := arrow.check_event(event)) is not None:
                return a

        for level in levels:
            level.draw(screen)
        arrow.draw(screen)
        pg.display.flip()
        clock.tick(FPS)
