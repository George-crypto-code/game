import pygame as pg
from settings import *
from player import Player
from enemy import Enemy
from world_map import Map
from box import Box
from load_image import load_image

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((WIGHT_OF_SCREEN, HEIGHT_OF_SCREEN))


# class borders
class Border(pg.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_borders)
        if x1 == x2:
            self.image = pg.Surface([1, y2 - y1])
            self.rect = pg.Rect(x1, y1, 1, y2 - y1)
        else:
            self.image = pg.Surface([x2 - x1, 1])
            self.rect = pg.Rect(x1, y1, x2 - x1, 1)
        self.mask = pg.mask.from_surface(self.image)


# set player
player_sprites = pg.sprite.Group()
player = Player(player_sprites)
# set enemies
enemy_sprites = pg.sprite.Group()
Enemy(enemy_sprites, (600, 300))
Enemy(enemy_sprites, (320, 200))
Enemy(enemy_sprites, (350, 350))
Enemy(enemy_sprites, (520, 80))
Enemy(enemy_sprites, (250, 400))
# set map
map_sprites = pg.sprite.Group()
_ = Map(map_sprites)
# set boxes
all_boxes = pg.sprite.Group()
Box(all_boxes, (100, 50))
Box(all_boxes, (450, 100))
Box(all_boxes, (540, 540))
Box(all_boxes, (250, 200))
# set borders
all_borders = pg.sprite.Group()
horizontal_top_borders = Border(0, 0, WIGHT_OF_MAP - 1, 0)
horizontal_bot_borders = Border(0, HEIGHT_OF_MAP - 1, WIGHT_OF_MAP - 1, HEIGHT_OF_MAP - 1)
vertical_left_borders = Border(0, 0, 0, HEIGHT_OF_MAP - 1)
vertical_right_borders = Border(WIGHT_OF_MAP - 1, 0, WIGHT_OF_MAP - 1, HEIGHT_OF_MAP - 1)

# aim
aim_image = pg.transform.scale(load_image("aim.png"), (20, 20))
mouse_pos = (0, 0)

# main gaming cycle
while True:
    screen.fill('black')
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.MOUSEMOTION:
            mouse_pos = event.pos
            pg.mouse.set_visible(False)

    # update player
    player.change_angle(mouse_pos)
    # check player and borders
    player.movement((horizontal_top_borders, horizontal_bot_borders, vertical_left_borders, vertical_right_borders),
                    all_boxes)
    # update enemies
    enemy_sprites.update()

    # drawing all things
    map_sprites.draw(screen)
    player_sprites.draw(screen)
    enemy_sprites.draw(screen)
    all_borders.draw(screen)
    all_boxes.draw(screen)
    # drawing aim
    if pg.mouse.get_focused():
        screen.blit(aim_image, mouse_pos)

    # system
    clock.tick(FPS)
    pg.display.flip()
