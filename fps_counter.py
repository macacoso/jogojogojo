import pygame

class FpsCounter:
    def __init__(self, start, assets):
        self.font = assets.font 
        self.textpos = pygame.Vector2(10, 10)
        self.start = start
        self.textpos2 = pygame.Vector2(10, 45)

    def render(self, screen, now, fps):
        survival = now - self.start

        text = self.font.render(f"fps: {round(fps)}", True, (255, 255, 255), (0, 0, 0))
        text2 = self.font.render(f"SU: {round(survival, 1)}s", True, (255, 255, 255), (0, 0, 0))
        screen.blit(text, self.textpos)
        screen.blit(text2, self.textpos2)