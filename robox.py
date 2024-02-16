import pygame, time
from all_particles import CoreParticle
class Robox(pygame.sprite.Sprite):
    def __init__(self, pos, lifetime, game, assets):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = assets.robox
        self.original_image = self.image
        self.image = pygame.transform.scale(self.image, (20 * 4, 21 * 4))
        self.size = 6
        self.pos = pos
        self.rect = self.image.get_rect(center=self.pos)
        self.rect_hitbox = pygame.Rect(0, 0, self.image.get_size()[0] * 0.5, self.image.get_size()[1] * 0.5)
        self.rect_hitbox.center = self.rect.center
        self.creation = time.monotonic()
        self.lifetime = lifetime
        self.particle_timer = 0
        self.particle_interval = 1 - self.size / 3
        
    def update(self, next_pos, dt, now, speed):
        self.particle_timer += dt
        if self.particle_timer >= self.particle_interval:    
            for i in range(int(self.size / 2)):
                particle = CoreParticle(pygame.Vector2(self.rect.centerx, self.rect.centery), pygame.color.Color(244, 81, 30))
                self.game.particles.append(particle)
            self.particle_timer = 0

        if self.pos != next_pos:
            self.pos += (pygame.Vector2(next_pos) - self.pos) * speed * dt 
        self.rect = self.image.get_rect(center=self.pos)
        self.rect_hitbox.center = self.rect.center
        if now - self.creation >= self.lifetime:
            self.kill()