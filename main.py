import csv
import pygame as pg
from time import sleep
from system_files.settings import *
from system_files.screen_files.load_image import load_image
from system_files.screen_files.start_screen import start_screen
from system_files.screen_files.menu_screen import menu_screen
from system_files.screen_files.victory_screen import victory_screen
from system_files.screen_files.lose_screen import lose_screen
from system_files.screen_files.options_screen import options_screen
from system_files.character_files.health import Health
from levels.level_1 import AllSprites as AllSprites_1
from levels.level_2 import AllSprites as AllSprites_2
from levels.level_3 import AllSprites as AllSprites_3
from levels.level_4 import AllSprites as AllSprites_4
from levels.level_5 import AllSprites as AllSprites_5
from levels.level_6 import AllSprites as AllSprites_6


def choose_level_sprites(level):
    if level == 1:  # import level which player chose
        return AllSprites_1(all_sprites, screen)  # the chosen level
    elif level == 2:
        return AllSprites_2(all_sprites, screen)
    elif level == 3:
        return AllSprites_3(all_sprites, screen)
    elif level == 4:
        return AllSprites_4(all_sprites, screen)
    elif level == 5:
        return AllSprites_5(all_sprites, screen)
    elif level == 6:
        return AllSprites_6(all_sprites, screen)


def start(screen, clock):  # func for start screen when player in it
    pg.mixer.music.unpause()
    while ans := start_screen(screen, clock):  # enter screen
        if ans == "play":  # if player choose the play btn than screen close
            return
        elif ans == "options":  # if player choose the options than open options screen
            options_screen(screen, clock)
            pg.mixer.music.set_volume(update_loud_of_game()[1])
        else:
            sleep(0.5)
            exit()


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
    pg.mixer.music.pause()
    shoot = pg.mixer.Sound(r'data/sounds/sound_effects/shoot.wav')
    hit = pg.mixer.Sound(r'data/sounds/sound_effects/hit.wav')
    shoot_miss = pg.mixer.Sound(r'data/sounds/sound_effects/shoot_miss.wav')
    SOUND_LOUD_OF_GAME = update_loud_of_game()[0]
    SHOOT_EVENT_TYPE = pg.USEREVENT + 1
    pg.time.set_timer(SHOOT_EVENT_TYPE, 1000)
    pos = (sprites.player.rect.x, sprites.player.rect.y)
    size = WIGHT_OF_SCREEN / 50, WIGHT_OF_SCREEN / 50
    shift = WIGHT_OF_SCREEN / 80
    player_health_bar = Health(load_image(("level_screen_images", "full_heard.png")), pos, size, shift)
    while True:
        shoot.set_volume(SOUND_LOUD_OF_GAME)
        hit.set_volume(SOUND_LOUD_OF_GAME)
        shoot_miss.set_volume(SOUND_LOUD_OF_GAME)
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
                SOUND_LOUD_OF_GAME = update_loud_of_game()[0]
                if ans == "home":
                    return "home"

            if event.type == SHOOT_EVENT_TYPE:
                for enemy in sprites.enemy_sprites:
                    enemy.shoot(sprites.player, sprites.all_boxes)

        if not sprites.enemy_sprites:
            return "win"

        if sprites.player.player_health <= 0:
            return "lose"
        # main method in each level
        all_sprites.update(mouse_pos)  # it updates all sprites and draw them
        player_health_bar.update((sprites.player.x, sprites.player.y))
        player_health_bar.draw(screen, sprites.player.player_health)

        # system
        clock.tick(FPS)
        pg.display.flip()


if __name__ == "__main__":
    pg.init()  # pygame initialization
    pg.mixer.init()  # for sound effects
    clock = pg.time.Clock()  # clock for tick of game
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)  # game screen
    pg.mixer.music.load(r"data\sounds\music\fon_music.mp3")
    pg.mixer.music.set_volume(update_loud_of_game()[1])
    pg.mixer.music.play(-1)
    level = prepare()
    while True:
        res = main(screen, clock, all_sprites, sprites, mouse_pos)
        pg.mouse.set_visible(True)
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
            if (victory_ans := victory_screen(screen, clock, level)) == "home":
                level = prepare()
            else:
                level += victory_ans
        elif res == "lose":
            lose_screen(screen, clock)
        all_sprites = pg.sprite.Group()
        sprites = choose_level_sprites(level)
        mouse_pos = (0, 0)
