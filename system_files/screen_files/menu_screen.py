import pygame as pg
import csv
from system_files.screen_files.load_image import load_image
from system_files.settings import *


def menu_screen(screen, clock):
    left, top = 150, 150
    # draw main fon
    fon = pg.transform.scale(load_image(('menu_screen_images', 'background.jpg')), (WIGHT_OF_SCREEN, HEIGHT_OF_SCREEN))
    screen.blit(fon, (0, 0))

    with open(r"data\levels.csv", encoding="utf8") as csvfile:
        data_levels = tuple(csv.reader(csvfile, delimiter=';', quotechar='"'))

    for i in range(1, 4):
        level_path = "complete_levels" if data_levels[i][1] == "1" else "levels"
        level = load_image(('menu_screen_images', level_path, f'level_{i}.png'))
        screen.blit(level, (left * (i), top))

    arrow = load_image(('menu_screen_images', 'arrow.png'))
    screen.blit(arrow, (10, 10))

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

            if event.type == pg.MOUSEMOTION:
                x, y = event.pos
                for i in range(1, 4):
                    level_path = "complete_levels" if data_levels[i][1] == "1" else "levels"
                    if left * i < x < left * i + 100 and top < y < top + 100:
                        level = load_image(('menu_screen_images', level_path, f'level_{i}_act.png'))
                    else:
                        level = load_image(('menu_screen_images', level_path, f'level_{i}.png'))
                    screen.blit(level, (left * i, top))

                if 10 < x < 86 and 10 < y < 86:
                    arrow = load_image(('menu_screen_images', 'arrow_act.png'))
                else:
                    arrow = load_image(('menu_screen_images', 'arrow.png'))
                screen.blit(arrow, (10, 10))

            if event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos
                for i in range(1, 4):
                    if left * i < x < left * i + 100 and top < y < top + 100:
                        return i
                if 10 < x < 86 and 10 < y < 86:
                    return 0
            pg.draw.rect(screen, "black", (100, 100, 600, 400), 3)

        pg.display.flip()
        clock.tick(FPS)
