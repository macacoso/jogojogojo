import pygame
import time
from bubble_shot import BubbleShot
from all_particles import ParticleExplosion
class WarningBubble(pygame.sprite.Sprite):
    def __init__(self, spawn_x, spawn_y, lifetime, bubble_lifetime, game, assets):
        pygame.sprite.Sprite.__init__(self)

        self.assets = assets
        self.initial_pos = pygame.Vector2(spawn_x, spawn_y)
        self.image = assets.bubble_warning
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.image_original = self.image
        self.rect = self.image.get_rect(center=self.initial_pos)
        self.rect_hitbox = pygame.Rect(0, 0, 20, 20)
        self.rect_hitbox.center = self.rect.center
        self.pos = pygame.Vector2(self.rect.center)
        self.creation_time = time.monotonic()
        self.lifetime = lifetime
        self.bubble_lifetime = bubble_lifetime
        self.inflate = 1
        self.turn = True
        self.game = game
        for i in range(10):
            particle = ParticleExplosion(pygame.Vector2(self.rect.centerx, self.rect.centery), pygame.color.Color(255, 0, 80))
            game.particles.append(particle)

    def update(self, now):
        if self.inflate < 1.25 and self.turn == True:
            self.inflate += 0.01
            self.image = pygame.transform.scale(self.image_original, (32 * self.inflate, 32 * self.inflate))
            self.rect = self.image.get_rect(center=self.initial_pos)
            self.rect_hitbox.center = self.rect.center
            if self.inflate >= 1.25:
                self.turn = False
        elif self.inflate > 0.75 and self.turn == False:
            self.inflate -= 0.01
            self.image = pygame.transform.scale(self.image_original, (32 * self.inflate, 32 * self.inflate))
            self.rect = self.image.get_rect(center=self.initial_pos)
            self.rect_hitbox.center = self.rect.center
            if self.inflate <= 0.75:
                self.turn = True

        if now - self.creation_time >= self.lifetime:
            bubble_shot = BubbleShot(self.initial_pos.x, self.initial_pos.y, self.bubble_lifetime, self.assets)
            self.game.bubble_shots.add(bubble_shot)
            self.game.sprites.add(bubble_shot)
            for i in range(10):
                particle = ParticleExplosion(pygame.Vector2(self.rect.centerx, self.rect.centery), pygame.color.Color(0, 150, 255))
                self.game.particles.append(particle)
            self.kill()
        self.rect.center = self.pos
        self.rect_hitbox.center = self.rect.center