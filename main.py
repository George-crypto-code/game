import pygame as pg
from settings import *
from player import Player

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((WIGHT_OF_SCREEN, HEIGHT_OF_SCREEN))
player_sprites = pg.sprite.Group()
player = Player(player_sprites)

# main gaming cycle
while True:
    screen.fill('black')
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.MOUSEMOTION:
            player.change_angle(event.pos)

    player.movement()
    player_sprites.draw(screen)
    clock.tick(FPS)
    pg.display.flip()
