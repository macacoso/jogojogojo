import pygame
import math
import time
from chasing_shots import ChasingShot
from all_particles import ParticleExplosion
class AimingShot(pygame.sprite.Sprite):
    def __init__(self, spawn_x, spawn_y, player_pos, lifetime, shot_speed, game, assets):
        pygame.sprite.Sprite.__init__(self)
        self.assets = assets
        self.image = assets.chasing_shot
        self.image = pygame.transform.scale(self.image, (18, 30))
        self.original_image = self.image
        self.initial_pos = pygame.Vector2(spawn_x, spawn_y)

        self.direction_vector = player_pos - self.initial_pos

        if self.direction_vector == pygame.Vector2(0, 0):
            self.direction_vector = pygame.Vector2(1, 0)
        else:
            self.direction_vector.normalize_ip()

        angle = math.degrees(math.atan2(self.direction_vector.y, self.direction_vector.x))

        self.image = pygame.transform.rotate(self.image, -angle - 90)

        self.rect = self.image.get_rect(center=self.initial_pos)
        self.rect_hitbox = pygame.Rect(0, 0, 10, 10)
        self.rect_hitbox.center = self.rect.center
        self.pos = pygame.Vector2(self.rect.center)
        self.game = game
        self.lifetime = lifetime
        self.creation_time = time.monotonic()
        self.shot_speed = shot_speed

    def update(self, player_pos, now):

        self.direction_vector = player_pos - self.initial_pos

        if self.direction_vector == pygame.Vector2(0, 0):
            self.direction_vector = pygame.Vector2(1, 0)
        else:
            self.direction_vector.normalize_ip()

        angle = math.degrees(math.atan2(self.direction_vector.y, self.direction_vector.x))
        self.image = pygame.transform.rotate(self.original_image, -angle - 90)
        self.rect.center = self.pos
        self.rect_hitbox.center = self.rect.center
        if now - self.creation_time >= self.lifetime:
            chasing_shot = ChasingShot(self.initial_pos.x, self.initial_pos.y, player_pos, self.shot_speed, self.game, self.assets)
            self.game.chasing_shots.add(chasing_shot)
            self.game.sprites.add(chasing_shot)
            for i in range(5):
                particle = ParticleExplosion(pygame.Vector2(self.rect.centerx, self.rect.centery), pygame.color.Color(255, 255, 255))
                self.game.particles.append(particle)
            self.kill()