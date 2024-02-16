import pygame, sys
from game_state import GameState
from level_select import show_level_menu
def showgameover(assets, screen, seconds, level):
    title = assets.font.render("GAME OVER", True, (255, 255, 255))
    text = assets.font.render(f"TIME SURVIVED: {round(seconds, 2)}s", True, (255, 255, 255))
    title_pos = title.get_rect(centerx=screen.get_width()/2, centery=screen.get_height()/2 - 150)
    text_pos = text.get_rect(centerx=screen.get_width()/2, centery=screen.get_height()/2 -100)
    button1 = pygame.Rect(screen.get_width()/2, screen.get_height() / 2, 300, 100)
    button1.centerx = screen.get_width()/2
    button1.centery = screen.get_height()/2
    button1_text = assets.font.render("RETRY", True, (255, 255, 255))
    button1_text_pos = button1_text.get_rect(centerx=button1.centerx, centery=button1.centery)
    button2 = pygame.Rect(screen.get_width()/2, screen.get_height()/2 + 150, 300, 100)
    button2.centerx = screen.get_width()/2
    button2.centery = screen.get_height()/2 + 150
    button2_text = assets.font.render("LEVEL SELECT", True, (255, 255, 255))
    button2_text_pos = button2_text.get_rect(centerx=button2.centerx, centery=button2.centery)
    button3 = pygame.Rect(screen.get_width()/2, screen.get_height()/2 + 300, 300, 100)
    button3.centerx=screen.get_width()/2
    button3.centery=screen.get_height()/2+300
    button3_text = assets.font.render("QUIT", True, (255, 255, 255))
    button3_text_pos = button3_text.get_rect(centerx=button3.centerx, centery=button3.centery)
    running = False
    while not running:
        screen.fill("black")
        events = pygame.event.get()
        a, b = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button1.x <= a <= button1.x + 300 and button1.y <= b <= button1.y + 100:
                return GameState(level, screen, assets)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button2.x <= a <= button2.x + 300 and button2.y <= b <= button2.y + 100:
                return GameState(show_level_menu(assets, screen, False), screen, assets)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button3.x <= a <= button3.x + 300 and button3.y <= b <= button3.y + 100:
                pygame.quit()
                sys.exit()
        if button1.x <= a <= button1.x + 300 and button1.y <= b <= button1.y + 100:
                pygame.draw.rect(screen, (255, 0, 0), button1)
        else:
                pygame.draw.rect(screen, (100, 0, 0), button1)
        if button2.x <= a <= button2.x + 300 and button2.y <= b <= button2.y + 100:
                pygame.draw.rect(screen, (255, 0, 0), button2)
        else:
                pygame.draw.rect(screen, (100, 0, 0), button2)
        if button3.x <= a <= button3.x + 300 and button3.y <= b <= button3.y + 100:
                pygame.draw.rect(screen, (255, 0, 0), button3)
        else:
                pygame.draw.rect(screen, (100, 0, 0), button3)
        screen.blit(title, title_pos)
        screen.blit(text, text_pos)
        screen.blit(button1_text, button1_text_pos)
        screen.blit(button2_text, button2_text_pos)
        screen.blit(button3_text, button3_text_pos)
        pygame.display.flip()
    return 
