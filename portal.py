import pygame
from all_particles import PortalParticle
class Portal(pygame.sprite.Sprite):
    def __init__(self, pos, game, assets):
        pygame.sprite.Sprite.__init__(self)
        portal_open = assets.portal_activate
        self.image = assets.portal
        self.image = pygame.transform.scale(self.image, (18 * 3, 18 * 3))
        self.rect = self.image.get_rect(center=pos)
        self.size = pygame.Vector2(self.image.get_size()[0], self.image.get_size()[1])
        self.rect_hitbox = pygame.Rect(0, 0, 18 * 2, 18 * 2)
        self.rect_hitbox.center = self.rect.center
        self.particle_timer = 0
        self.particle_interval = 0.15
        self.game = game
        portal_open.play()

    def update(self, dt):
        self.particle_timer += dt
        if self.particle_timer >= self.particle_interval:
            for i in range(5):
                particle = PortalParticle(pygame.Vector2(self.rect.centerx, self.rect.centery), self.size)
                self.game.portal_particles.append(particle)
            self.particle_timer = 0