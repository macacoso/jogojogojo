import pygame
import time
from spitter import Spitter
from all_particles import ParticleExplosion
class WarningSign(pygame.sprite.Sprite):
    def __init__(self, spawn_x, spawn_y, lifetime, spitter_lifetime, spitter_speed, spitter_shot_interval, spitter_shot_speed, spitter_type, game):
        pygame.sprite.Sprite.__init__(self)

        self.initial_pos = pygame.Vector2(spawn_x, spawn_y)
        self.image = game.assets.warning_sign
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.image_original = self.image
        self.rect = self.image.get_rect(center=self.initial_pos)
        self.rect_hitbox = pygame.Rect(0, 0, 20, 20)
        self.rect_hitbox.center = self.rect.center
        self.pos = pygame.Vector2(self.rect.center)
        self.creation_time = time.monotonic()
        self.lifetime = lifetime
        self.spitter_lifetime = spitter_lifetime
        self.spitter_speed = spitter_speed
        self.inflate = 1
        self.turn = True
        self.game = game
        self.assets = self.game.assets
        self.spitter_shot_interval = spitter_shot_interval
        self.spitter_shot_speed = spitter_shot_speed
        self.spitter_type = spitter_type

    def update(self, now):
        if self.inflate < 1.15 and self.turn == True:
            self.inflate += 0.01
            self.image = pygame.transform.scale(self.image_original, (32 * self.inflate, 32 * self.inflate))
            self.rect = self.image.get_rect(center=self.initial_pos)
            self.rect_hitbox.center = self.rect.center
            if self.inflate >= 1.15:
                self.turn = False
        elif self.inflate > 0.85 and self.turn == False:
            self.inflate -= 0.01
            self.image = pygame.transform.scale(self.image_original, (32 * self.inflate, 32 * self.inflate))
            self.rect = self.image.get_rect(center=self.initial_pos)
            self.rect_hitbox.center = self.rect.center
            if self.inflate <= 0.85:
                self.turn = True
        if now - self.creation_time >= self.lifetime:
            enemy = Spitter(self.initial_pos.x, self.initial_pos.y, self.spitter_lifetime, self.spitter_speed, self.spitter_shot_interval, self.spitter_shot_speed, self.spitter_type, self.game)
            self.game.enemies.add(enemy)
            self.game.player_sprite.add(enemy)
            for i in range(30):
                particle = ParticleExplosion(pygame.Vector2(self.rect.centerx, self.rect.centery), pygame.color.Color(255, 255, 255))
                self.game.particles.append(particle) 
            self.kill()
        self.rect.center = self.pos
        self.rect_hitbox.center = self.rect.center