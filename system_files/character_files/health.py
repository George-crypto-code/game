import pygame as pg


class Health:
    def __init__(self, image_1, pos=(0, 0), size=(100, 100), shift=0):
        self.shift = shift
        self.size = size
        self.pos = pos
        self.full_image = pg.transform.scale(image_1, self.size)

    def draw(self, screen, curr_health):
        for i in range(curr_health):
            screen.blit(self.full_image, (self.pos[0] + self.shift * i, self.pos[1]))

    def update(self, pos):
        self.pos = pos
