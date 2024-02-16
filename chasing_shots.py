import pygame
import math
from all_particles import ParticleTrail, ParticleExplosion
class ChasingShot(pygame.sprite.Sprite):
    def __init__(self, spawn_x, spawn_y, player_pos, shot_speed, game, assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets.chasing_shot
        self.image = pygame.transform.scale(self.image, (18, 30))

        self.initial_pos = pygame.Vector2(spawn_x, spawn_y)

        direction_vector = player_pos - self.initial_pos

        if direction_vector == pygame.Vector2(0, 0):
            direction_vector = pygame.Vector2(1, 0)
        else:
            direction_vector.normalize_ip()

        angle = math.degrees(math.atan2(direction_vector.y, direction_vector.x))

        self.image = pygame.transform.rotate(self.image, -angle - 90)

        self.rect = self.image.get_rect(center=self.initial_pos)
        self.rect_hitbox = pygame.Rect(0, 0, 10, 10)
        self.rect_hitbox.center = self.rect.center
        self.pos = pygame.Vector2(self.rect.center)
        self.speed = pygame.math.Vector2(shot_speed, 0).rotate(angle)
        self.game = game

    def update(self, dt):
        for i in range(1):
            particle = ParticleTrail(pygame.Vector2(self.rect.centerx, self.rect.centery), pygame.color.Color(0, 150, 255))
            self.game.particles.append(particle)
        self.pos += self.speed * dt
        self.rect.center = self.pos
        self.rect_hitbox.center = self.rect.center
