import pygame as pg
from settings import *
from player import Player
from map import Map

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((WIGHT_OF_SCREEN, HEIGHT_OF_SCREEN))
# set player
player_sprites = pg.sprite.Group()
player = Player(player_sprites)
# set map
map_sprites = pg.sprite.Group()
map = Map(map_sprites)

pos = (0, 0)

# main gaming cycle
while True:
    screen.fill('black')
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.MOUSEMOTION:
            pos = event.pos

    # update player
    player.change_angle(pos)
    player.movement()

    # drawing all things
    map_sprites.draw(screen)
    player_sprites.draw(screen)

    # system
    clock.tick(FPS)
    pg.display.flip()
