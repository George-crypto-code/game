import pygame as pg
from settings import *
from player import Player
from map import Map
from load_image import load_image

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((WIGHT_OF_SCREEN, HEIGHT_OF_SCREEN))
# set player
player_sprites = pg.sprite.Group()
player = Player(player_sprites)
# set map
map_sprites = pg.sprite.Group()
_ = Map(map_sprites)
# aim
aim_image = pg.transform.scale(load_image("aim.png"), (20, 20))

# main gaming cycle
while True:
    screen.fill('black')
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.MOUSEMOTION:
            pos = event.pos
            pg.mouse.set_visible(False)

    # update player
    player.change_angle(pos)
    player.movement()

    # drawing all things
    map_sprites.draw(screen)
    player_sprites.draw(screen)

    if pg.mouse.get_focused():
        screen.blit(aim_image, pos)

    # system
    clock.tick(FPS)
    pg.display.flip()
