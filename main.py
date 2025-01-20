import csv
import pygame as pg
from system_files.settings import *
from system_files.start_screen import start_screen
from system_files.screen_files.menu_screen import menu_screen
from system_files.screen_files.lose_screen import lose_screen
from system_files.screen_files.options_screen import options_screen
from levels.level_1 import AllSprites as AllSprites_1
from levels.level_2 import AllSprites as AllSprites_2
from levels.level_3 import AllSprites as AllSprites_3


def choose_level_sprites(level):
    if level == 1:  # import level which player chose
        return AllSprites_1(all_sprites, screen)  # the chosen level
    elif level == 2:
        return AllSprites_2(all_sprites, screen)
    elif level == 3:
        return AllSprites_3(all_sprites, screen)


def start(screen, clock):  # func for start screen when player in it
    while ans := start_screen(screen, clock):  # enter screen
        if ans == "play":  # if player choose the play btn than screen close
            return
        elif ans == "options":  # if player choose the options than open options screen
            options_screen(screen, clock)


def prepare():
    global all_sprites, sprites, mouse_pos
    pg.mouse.set_visible(True)
    start(screen, clock)  # start screen
    while not (level_of_game := menu_screen(screen, clock)):  # while player not choose the level, menu not hide
        start(screen, clock)  # if player choose the arrow back
    all_sprites = pg.sprite.Group()  # all sprites for more readable code and it eazy to refix levels
    sprites = choose_level_sprites(level_of_game)
    mouse_pos = (0, 0)
    return level_of_game


def main(screen, clock, all_sprites, sprites, mouse_pos):
    # main gaming cycled
    shoot = pg.mixer.Sound(r'data/sounds/sound_effects/shoot.wav')
    hit = pg.mixer.Sound(r'data/sounds/sound_effects/hit.wav')
    shoot_miss = pg.mixer.Sound(r'data/sounds/sound_effects/shoot_miss.wav')
    LOUD_OF_GAME = update_loud_of_game()
    while True:
        shoot.set_volume(LOUD_OF_GAME)
        hit.set_volume(LOUD_OF_GAME)
        shoot_miss.set_volume(LOUD_OF_GAME)
        screen.fill('black')
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.MOUSEMOTION:
                mouse_pos = event.pos
                pg.mouse.set_visible(False)

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if enemy := sprites.aim_image.check_shoot(
                        sprites.enemy_sprites):  # if aim collide with enemy than raise shoot method
                    if sprites.player.shoot(event.pos, enemy, sprites.all_boxes):
                        shoot.play()
                        hit.play()
                    else:
                        shoot_miss.play()
                else:
                    shoot.play()

            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                pg.mouse.set_visible(True)
                ans = options_screen(screen, clock)
                LOUD_OF_GAME = update_loud_of_game()
                if ans == "home":
                    return "home"

        if not sprites.enemy_sprites:
            return "win"

        if sprites.player.player_health <= 0:
            pg.mouse.set_visible(True)
            lose_screen(screen, clock)
            return "lose"
        # main method in each level
        all_sprites.update(mouse_pos)  # it updates all sprites and draw them

        # system
        clock.tick(FPS)
        pg.display.flip()


if __name__ == "__main__":
    pg.init()  # pygame initialization
    pg.mixer.init()  # for sound effects
    clock = pg.time.Clock()  # clock for tick of game
    screen = pg.display.set_mode((WIGHT_OF_SCREEN, HEIGHT_OF_SCREEN))  # game screen
    level = prepare()
    while True:
        res = main(screen, clock, all_sprites, sprites, mouse_pos)
        if res == "home":
            level = prepare()
        elif res == "win":
            with open(r"data\levels.csv", encoding="utf8") as csvfile:
                data_levels = list(csv.reader(csvfile, delimiter=';', quotechar='"'))
            data_levels[level][1] = "1"
            with open(r"data\levels.csv", mode="w", newline='', encoding="utf8") as csvfile:
                writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                for string in data_levels:
                    writer.writerow(string)
            level = prepare()
        elif res == "lose":
            all_sprites = pg.sprite.Group()
            sprites = choose_level_sprites(level)
            mouse_pos = (0, 0)
