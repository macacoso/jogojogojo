import pygame
import time
import math
from shock_shots import ShockShot
from all_particles import ParticleExplosion
class Spitter(pygame.sprite.Sprite):
    def __init__(self, spawn_x, spawn_y, lifetime, speed, shot_interval, shot_speed, type, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.initial_pos = pygame.Vector2(spawn_x, spawn_y)
        self.image = game.assets.spitter
        self.image = pygame.transform.scale(self.image, (16 * 2, 14 * 2))
        self.rect = self.image.get_rect(center=self.initial_pos)
        self.rect_hitbox = pygame.Rect(0, 0, 20, 20)
        self.rect_hitbox.center = self.rect.center
        self.creation_time = time.monotonic()
        self.pos = pygame.Vector2(self.rect.center)
        self.lifetime = lifetime
        self.speed = speed
        self.type = type
        self.shot_interval = shot_interval
        self.shot_timer = 0
        self.shot_speed = shot_speed
        self.turn = False

    def update(self, player, dt, now):
        self.shot_timer += dt
        if now - self.creation_time >= self.lifetime:
            for i in range(15):
                particle = ParticleExplosion(pygame.Vector2(self.rect.centerx, self.rect.centery), pygame.color.Color(244, 81, 30))
                self.game.particles.append(particle)
            self.kill()
        player_vec = pygame.Vector2(player.rect_hitbox.center)
        self.pos = self.pos.move_towards(player_vec, self.speed * dt)
        self.rect = self.image.get_rect(center=self.pos)
        self.rect_hitbox.center = self.rect.center
        if self.shot_timer >= self.shot_interval:
            if self.type == 1:
                self.nova8()
            elif self.type == 2:
                self.nova16()
            self.shot_timer = 0

    def nova8(self):
        for i in range(8):
            if self.turn == False:
                angle = i * (360 / 8)
                self.turn = True if i == 7 else False
            else:
                angle = i * (360 / 8) + 22.5
                self.turn = False if i == 7 else True
            direction_x = round(math.cos(math.radians(angle)), 2)
            direction_y = round(math.sin(math.radians(angle)), 2)
            direction = pygame.Vector2(direction_x, direction_y)
            
            shock_shot = ShockShot(self.pos.x, self.pos.y, direction, self.shot_speed, self.game.assets)
            self.game.shock_shots.add(shock_shot)
            self.game.sprites.add(shock_shot)

        for i in range(5):
            particle = ParticleExplosion(pygame.Vector2(self.rect.centerx, self.rect.centery), pygame.color.Color(244, 81, 30))
            self.game.particles.append(particle)

    def nova16(self):
        for i in range(16):
            if self.turn == False:
                angle = i * (360 / 16)
                self.turn = True if i == 15 else False
            else:
                angle = i * (360 / 16) + 11.25
                self.turn = False if i == 15 else True
            direction_x = round(math.cos(math.radians(angle)), 2)
            direction_y = round(math.sin(math.radians(angle)), 2)
            direction = pygame.Vector2(direction_x, direction_y)
            
            shock_shot = ShockShot(self.pos.x, self.pos.y, direction, self.shot_speed, self.game.assets)
            self.game.shock_shots.add(shock_shot)
            self.game.sprites.add(shock_shot)
        
        for i in range(10):
            particle = ParticleExplosion(pygame.Vector2(self.rect.centerx, self.rect.centery), pygame.color.Color(244, 81, 30))
            self.game.particles.append(particle)