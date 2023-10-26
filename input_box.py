import pygame
from settings import *

class InputBox:
    def __init__(self, x, y, width, height):
        pygame.font.init()
        self.rect = pygame.Rect(x, y, width, height)
        self.text = ""
        self.active = False

        self.font = pygame.font.Font(None, 32)

        self.info_text = "Type city in:"
        self.info_text_surf = self.font.render(self.info_text, True, "white")

    def show_info(self):
        SCREEN.blit(self.info_text_surf, (50,10))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        elif event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    return self.text
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def return_text(self):
        return self.text

    def draw(self, screen):
        color = (255, 255, 255) if self.active else (222, 222, 222)
        pygame.draw.rect(screen, color, self.rect, 4)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        screen.blit(text_surface, (self.rect.x + 10, self.rect.y + 10))

    def update(self):
        self.draw(SCREEN)
        self.show_info()

input_box = InputBox(20, 35, 200, 40)