import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, axis):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((width, height))
        self.image.fill((color))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.axis = axis