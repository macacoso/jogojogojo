import pygame

class HpCounter:
    def __init__(self, assets):
        self.font = assets.font
        self.container = pygame.Rect(1400, 350, 300, 50)
        self.bar = pygame.Rect(1400, 350, 300, 50)


    def render(self, screen, hp, max_hp):
        hp_100 = 100 * hp / max_hp
        red = int(3825 / hp_100)
        green = int(255 * hp_100 / 100)
        # print (red, green)
        if hp_100 <= 15:
            color = pygame.Color(255, green, 0)
        else:
            color = pygame.Color(red, green, 0)
        
        text = self.font.render(f"HP: {round(hp)}/{round(max_hp)}", True, (0, 0, 0))
        textpos = text.get_rect(centerx=1400, centery=350)
        self.bar.width = 3 * hp_100
        self.bar.topleft = (1250, 325)
        self.container.center = (1400, 350)
        pygame.draw.rect(screen, (38, 50, 56), self.container)
        pygame.draw.rect(screen, color, self.bar)
        screen.blit(text, textpos)

# formula green: x = (255 * hp%) / 100
# formula red: x = 
# formula width = 3 * hp%
# formula hp% = (100 * hp) / max_hp
# 
#
#        