import pygame as pg


class Border(pg.sprite.Sprite):
    def __init__(self, all_borders, x1, y1, x2, y2):
        super().__init__(all_borders)
        if x1 == x2:
            self.image = pg.Surface([1, y2 - y1])
            self.rect = pg.Rect(x1, y1, 1, y2 - y1)
        else:
            self.image = pg.Surface([x2 - x1, 1])
            self.rect = pg.Rect(x1, y1, x2 - x1, 1)
        self.mask = pg.mask.from_surface(self.image)
