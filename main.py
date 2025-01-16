import pygame as pg
from system_files.settings import *
from system_files.start_screen import start_screen
from system_files.menu_screen import menu_screen
from system_files.lose_screen import lose_screen
from system_files.options_screen import options_screen


def start(screen, clock):  # func for start screen when player in it
    while ans := start_screen(screen, clock):  # enter screen
        if ans == "play":  # if player choose the play btn than screen close
            return
        elif ans == "options":  # if player choose the options than open options screen
            options_screen(screen, clock, LOUD_OF_GAME)


def prepare():
    global screen, clock, all_sprites, sprites, mouse_pos, AllSprites
    start(screen, clock)  # start screen
    while not (level := menu_screen(screen, clock)):  # while player not choose the level, menu not hide
        start(screen, clock)  # if player choose the arrow back

    if level == 1:  # import level which player chose
        from levels.level_1 import AllSprites

    all_sprites = pg.sprite.Group()  # all sprites for more readable code and it eazy to refix levels
    sprites = AllSprites(all_sprites, screen)  # the chosen level
    mouse_pos = (0, 0)


def main(screen, clock, all_sprites, sprites, mouse_pos):
    # main gaming cycled
    while True:
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
                        pg.mixer.Sound(r'data\sounds\shoot.wav').play().set_volume(LOUD_OF_GAME)
                        pg.mixer.Sound(r'data\sounds\hit.wav').play().set_volume(LOUD_OF_GAME)
                    else:
                        pg.mixer.Sound(r'data\sounds\shoot_miss.wav').play().set_volume(LOUD_OF_GAME)
                else:
                    pg.mixer.Sound(r'data\sounds\shoot.wav').play().set_volume(LOUD_OF_GAME)

            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                pg.mouse.set_visible(True)
                ans = options_screen(screen, clock, LOUD_OF_GAME)
                if ans == 1:
                    return "home"

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
    prepare()
    while True:
        res = main(screen, clock, all_sprites, sprites, mouse_pos)
        if res == "lose":
            all_sprites = pg.sprite.Group()
            sprites = AllSprites(all_sprites, screen)
            mouse_pos = (0, 0)
        elif res == "home":
            prepare()
