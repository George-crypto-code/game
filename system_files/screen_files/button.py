import pygame as pg


class Button:
    def __init__(self, image_default, hover_image=None, signal=None, pos=(0, 0), wight=100, height=100):
        super().__init__()
        self.pos = pos
        self.wight, self.height = wight, height
        self.image_default = pg.transform.scale(image_default, (self.wight, self.height))
        self.rect = self.image_default.get_rect()
        self.hover_image = pg.transform.scale(hover_image, (self.wight, self.height))
        self.signal = signal
        self.is_hovered = False

    def draw(self, screen):
        if self.is_hovered:
            curr_image = self.hover_image
        else:
            curr_image = self.image_default
        screen.blit(curr_image, self.pos)

    def check_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            x, y = event.pos
            i, j = self.pos
            if i < x < i + self.wight and j < y < j + self.height:
                return self.signal

        if event.type == pg.MOUSEMOTION:
            x, y = event.pos
            i, j = self.pos
            if i < x < i + self.wight and j < y < j + self.height:
                self.is_hovered = True
            else:
                self.is_hovered = False
        return None
