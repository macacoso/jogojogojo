import pygame, time
from all_particles import SnowParticle
class Snomin(pygame.sprite.Sprite):
    def __init__(self, pos, lifetime, game, assets):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = assets.snomin
        self.original_image = self.image
        self.image = pygame.transform.scale(self.image, (16 * 2, 8 * 2))
        self.size = 2
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
                particle = SnowParticle(pygame.Vector2(self.rect.centerx, self.rect.bottom + 1), self.size, pygame.color.Color(77, 189, 239))
                self.game.particles.append(particle)
            self.particle_timer = 0

        if self.pos != next_pos:
            self.pos += (pygame.Vector2(next_pos) - self.pos) * speed * dt 
        self.rect = self.image.get_rect(center=self.pos)
        self.rect_hitbox.center = self.rect.center
        if now - self.creation >= self.lifetime:
            self.kill()

    def grow(self, amount):
        self.size = amount
        self.image = pygame.transform.scale(self.original_image, (16 * self.size, 8 * self.size))
        self.rect_hitbox = pygame.Rect(0, 0, self.image.get_size()[0] * 0.5, self.image.get_size()[1] * 0.5)