import pygame, time

class UpHand(pygame.sprite.Sprite):
    def __init__(self, pos, lifetime, assets):
        pygame.sprite.Sprite.__init__(self)
    
        self.image = assets.snomin_hand_up
        self.image = pygame.transform.scale(self.image, (self.image.get_size()[0] * 3, self.image.get_size()[1] * 3))
        self.pos = pos
        self.rect = self.image.get_rect(center=self.pos)
        self.rect_hitbox = pygame.Rect(0, 0, 20, 20)
        self.rect_hitbox.center = self.rect.center
        self.turn = False
        self.timer = 0
        self.timer_interval = 0.75
        self.lifetime = lifetime
        self.creation_time = time.monotonic()

    def update(self, dt):
        self.timer += dt
        if self.timer >= self.timer_interval:
            if self.turn == False:
                self.pos.y += 5
                self.turn = True
            else:
                self.pos.y -= 5
                self.turn = False
            self.timer = 0
        self.rect = self.image.get_rect(center=self.pos)
        self.rect_hitbox.center = self.rect.center
        if time.monotonic() - self.creation_time >= self.lifetime:
            self.kill()


class DownHand(pygame.sprite.Sprite):
    def __init__(self, pos, lifetime, assets):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets.snomin_hand_down
        self.image = pygame.transform.scale(self.image, (self.image.get_size()[0] * 3, self.image.get_size()[1] * 3))
        self.pos = pos
        self.rect = self.image.get_rect(center=self.pos)
        self.rect_hitbox = pygame.Rect(0, 0, 20, 20)
        self.rect_hitbox.center = self.rect.center
        self.turn = True
        self.timer = 0
        self.timer_interval = 0.75
        self.lifetime = lifetime
        self.creation_time = time.monotonic()

    def update(self, dt):
        self.timer += dt
        if self.timer >= self.timer_interval:
            if self.turn == False:
                self.pos.y += 5
                self.turn = True
            else:
                self.pos.y -= 5
                self.turn = False
            self.timer = 0
        self.rect = self.image.get_rect(center=self.pos)
        self.rect_hitbox.center = self.rect.center
        if time.monotonic() - self.creation_time >= self.lifetime:
            self.kill()