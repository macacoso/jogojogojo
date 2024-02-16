import pygame, sys
def show_level_menu(assets, screen, running):
    title = assets.font.render("LEVEL SELECT", True, (255, 255, 255))
    title_pos = title.get_rect(centerx=screen.get_width()/2, centery=150)
    button1 = pygame.Rect(100, 200, 300, 100)
    button1_text = assets.font.render("TUTORIAL", True, (255, 255, 255))
    button1_text_pos = button1_text.get_rect(centerx=button1.centerx, centery=button1.centery)
    button2 = pygame.Rect(500, 200, 300, 100)
    button2_text = assets.font.render("LEVEL 1", True, (255, 255, 255))
    button2_text_pos = button2_text.get_rect(centerx=button2.centerx, centery=button2.centery)
    button3 = pygame.Rect(900, 200, 300, 100)
    button3_text = assets.font.render("LEVEL 2", True, (255, 255, 255))
    button3_text_pos = button3_text.get_rect(centerx=button3.centerx, centery=button3.centery)
    button4 = pygame.Rect(900, screen.get_height()/2 + 250, 300, 100)
    button4_text = assets.font.render("QUIT", True, (255, 255, 255))
    button4_text_pos = button4_text.get_rect(centerx=button4.centerx, centery=button4.centery)
    while not running:
        screen.fill("black")
        events = pygame.event.get()
        a, b = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button1.x <= a <= button1.x + 300 and button1.y <= b <= button1.y + 100:
                return 1
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button2.x <= a <= button2.x + 300 and button2.y <= b <= button2.y + 100:
                return 2
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button3.x <= a <= button3.x + 300 and button3.y <= b <= button3.y + 100:
                return 3
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button4.x <= a <= button4.x + 300 and button4.y <= b <= button4.y + 100:
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
        if button4.x <= a <= button4.x + 300 and button4.y <= b <= button4.y + 100:
              pygame.draw.rect(screen, (255, 0, 0), button4)
        else:
              pygame.draw.rect(screen, (100, 0, 0), button4)
        screen.blit(title, title_pos)
        screen.blit(button1_text, button1_text_pos)
        screen.blit(button2_text, button2_text_pos)
        screen.blit(button3_text, button3_text_pos)
        screen.blit(button4_text, button4_text_pos)
        pygame.display.flip()
    return True
