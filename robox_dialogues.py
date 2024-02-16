import pygame
import time
class Dialogues:
    def __init__(self, assets):
        self.start = time.monotonic()
        self.font = assets.font

    def render(self, screen):
        text = self.font.render("thief detected at factory #69", True, "white")
        textpos = text.get_rect(centerx = 860, centery = 230)
        text2 = self.font.render("initiating extermination protocol", True, "white")
        textpos2 = text2.get_rect(centerx = 860, centery = 260)
        screen.blit(text, textpos)
        screen.blit(text2, textpos2)

    def render2(self, screen):
        text = self.font.render("deploying spitter units", True, "white")
        textpos = text.get_rect(centerx = 860, centery = 480)
        screen.blit(text, textpos)