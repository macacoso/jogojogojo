import pygame, random

class ParticleHurt:
    def __init__(self, pos):
        self.pos = pos
        self.speed = pygame.Vector2(random.randint(0, 20) / 10 - 1, random.randint(0, 20)/10 - 1)
        self.timer = random.randint(5, 7)
        
    def update(self, screen):
        
        self.pos.x += self.speed.x
        self.pos.y += self.speed.y
        self.speed += (0, 0.1)
        self.timer -= 0.1
        pygame.draw.circle(screen, (255, 0, 0), (int(self.pos.x), int(self.pos.y)), int(self.timer))

class ParticleExplosion:
    def __init__(self, pos, color):
        self.pos = pos
        self.speed = pygame.Vector2(random.randint(0, 20) / 10 - 1, random.randint(0, 20)/10 -1)
        self.timer = random.randint(5, 7)
        self.color = color

    def update(self, screen):

        self.pos.x += self.speed.x
        self.pos.y += self.speed.y
        self.timer -= 0.1
        pygame.draw.circle(screen, self.color, (int(self.pos.x), int(self.pos.y)), int(self.timer))

    
class ParticleTrail:
    def __init__(self, pos, color):
        self.pos = pos
        # self.speed = pygame.Vector2(-speed.x, -speed.y)
        self.speed = pygame.Vector2(random.randint(0, 20) / 10 - 1, random.randint(0, 20)/10 -1)
        self.timer = random.randint(3, 5)
        self.color = color

    def update(self, screen):
        self.pos.x += self.speed.x
        self.pos.y += self.speed.y
        self.timer -= 0.1
        pygame.draw.circle(screen, self.color, (int(self.pos.x), int(self.pos.y)), int(self.timer))

class SnowParticle:
    def __init__(self, pos, size, color):
        self.pos = pygame.Vector2(pos.x + (random.randint(-size * 4, size * 4)), pos.y)
        self.speed = pygame.Vector2(random.randint(0, 20) / 15 - 1, random.randint(0, 10)/10)
        self.timer = random.randint(2, 4)
        self.color = color

    def update(self, screen):
        self.pos.x +=self.speed.x
        self.pos.y += self.speed.y
        self.timer -= 0.1
        pygame.draw.circle(screen, self.color, (int(self.pos.x), int(self.pos.y)), int(self.timer))

class PortalParticle:
    def __init__(self, pos, size):
        self.target = pos
        self.pos = pygame.Vector2(pos.x + (random.randrange(-size.x * 2, size.x * 2)), pos.y + (random.randrange(-size.y * 2, size.y * 2)))
        self.timer = random.randint(5, 7)

    def update(self, dt, screen):
        self.pos += (self.target - self.pos) * 2 * dt
        self.timer -= 0.1
        pygame.draw.circle(screen, (49, 27, 146), (int(self.pos.x), int(self.pos.y)), int(self.timer))

class CoreParticle:
    def __init__(self, pos, color):
        self.pos = pygame.Vector2(pos.x, pos.y)
        self.speed = pygame.Vector2(random.randint(-10, 10) / 10, random.randint(-10, 10)/10)
        self.timer = random.randint(2, 3)
        self.color = color

    def update(self, screen):
        self.pos.x +=self.speed.x
        self.pos.y += self.speed.y
        self.timer -= 0.1
        pygame.draw.circle(screen, self.color, (int(self.pos.x), int(self.pos.y)), int(self.timer))