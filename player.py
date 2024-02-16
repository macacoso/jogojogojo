import pygame
from all_particles import ParticleHurt
class Player(pygame.sprite.Sprite):
    def __init__(self, size, speed, vitality, hp, max_hp, screen, assets):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = assets.char
        self.image = pygame.transform.scale(self.image, (24, 32))
        self.size = size
        self.rect = self.image.get_rect()
        self.rect_hitbox = pygame.Rect(0, 0, 20, 20)
        self.rect.center = (screen.get_width()/2, screen.get_height()/2)
        self.rect_hitbox.center = self.rect.center
        self.speed = speed
        self.alive = True
        self.old_x = self.rect.x
        self.old_y = self.rect.y
        self.hp = hp
        self.max_hp = max_hp
        self.vitality = vitality
        self.hit_sound = assets.damage_sound

    def update(self, keys, dt):
        self.rect_hitbox.center = self.rect.center
        self.old_x = self.rect.x
        self.old_y = self.rect.y
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= self.speed * dt
            
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += self.speed * dt
            
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.rect.y -= self.speed * dt
            
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.rect.y += self.speed * dt
        
        if self.max_hp > self.hp:
            self.hp += self.vitality * dt
        
    def reduce_hp(self, game, qty):
        for i in range(10):
            particle = ParticleHurt(pygame.Vector2(self.rect.centerx, self.rect.centery))
            game.particles.append(particle)
        self.hp -= qty
        self.hit_sound.play()
        if self.hp <= 0: 
            self.kill()
        
    def kill(self):
        self.alive = False