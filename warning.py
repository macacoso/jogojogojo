import pygame, time

class Warning(pygame.sprite.Sprite):
    def __init__(self, pos, lifetime, size, assets):
        pygame.sprite.Sprite.__init__(self)
        self.initial_pos = pos
        self.image = assets.warning_sign
        self.image = pygame.transform.scale(self.image, (16 * size, 16 * size))
        self.image_original = self.image
        self.rect = self.image.get_rect(center=self.initial_pos)
        self.rect_hitbox = pygame.Rect(0, 0, 20, 20)
        self.rect_hitbox.center = self.rect.center
        self.pos = pygame.Vector2(self.rect.center)
        self.creation_time = time.monotonic()
        self.lifetime = lifetime
        self.inflate = 1
        self.turn = True
        self.size = size

    def update(self, now):
        if self.inflate < 1.15 and self.turn == True:
            self.inflate += 0.01
            self.image = pygame.transform.scale(self.image_original, (16 * self.size * self.inflate, 16 * self.size * self.inflate))
            self.rect = self.image.get_rect(center=self.initial_pos)
            self.rect_hitbox.center = self.rect.center
            if self.inflate >= 1.15:
                self.turn = False
        elif self.inflate > 0.85 and self.turn == False:
            self.inflate -= 0.01
            self.image = pygame.transform.scale(self.image_original, (16 * self.size * self.inflate, 16 * self.size * self.inflate))
            self.rect = self.image.get_rect(center=self.initial_pos)
            self.rect_hitbox.center = self.rect.center
            if self.inflate <= 0.85:
                self.turn = True
        if now - self.creation_time >= self.lifetime:
            self.kill()
        self.rect.center = self.pos
        self.rect_hitbox.center = self.rect.center