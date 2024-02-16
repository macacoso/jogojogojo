import pygame
import math

class ShockShot(pygame.sprite.Sprite):
    def __init__(self, spawn_x, spawn_y, direction, shot_speed, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets.shock_shot
        self.image = pygame.transform.scale(self.image, (16 * 2, 16 * 2))
        self.initial_pos = pygame.Vector2(spawn_x, spawn_y)
        direction_vector = direction
        # direction_vector.normalize_ip()
        angle = math.degrees(math.atan2(direction_vector.y, direction_vector.x))
        self.rect = self.image.get_rect(center=self.initial_pos)
        self.rect_hitbox = pygame.Rect(0, 0, 20, 20)
        self.rect_hitbox.center = self.rect.center
        self.pos = pygame.Vector2(self.rect.center)
        self.speed = pygame.math.Vector2(shot_speed, 0).rotate(angle)
        self.image = pygame.transform.rotate(self.image, -angle + 90)

    def update(self, dt):
        self.pos += self.speed * dt
        self.rect.center = self.pos
        self.rect_hitbox.center = pygame.Vector2(self.rect.centerx, self.rect.centery)
