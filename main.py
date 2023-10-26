import pygame as pg
from sys import exit
from settings import *
from information_getter import *
from input_box import *

class App:
    def __init__(self):
        pg.init()
        pg.font.init()

        pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption("Weather Information")

        icon_surf = pg.image.load("icon.png")
        pg.display.set_icon(icon_surf)

        self.clock = pg.time.Clock()

    def draw_window(self):
        SCREEN.fill("#488599")
        input_box.update()
        information_getter.update()

    def update(self):
        self.clock.tick(FPS)
        pg.display.update()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            else:
                input_box.handle_event(event)

    def run(self):
        while True:
            self.update()
            self.check_events()
            self.draw_window()

if __name__ == "__main__":
    app = App()
    app.run()