import pygame, sys
import time
import menu
from assets import Assets
from game_state import GameState
from fps_counter import FpsCounter
from game_over import showgameover
from instructions import Instructions
from hp_counter import HpCounter
from game_won import showgamewon

def pygame_init():
    pygame.mixer.init()
    pygame.mixer.set_num_channels(32)
    pygame.font.init()
    pygame.display.set_caption('SU')

def run():
    pygame_init()
    running = False
    screen = pygame.display.set_mode((1720, 960))
    assets = Assets()
    game = menu.show(assets, screen, running)


    while True:
        dt = game.clock.tick(60) / 1000
        fps = game.clock.get_fps()
        now = time.monotonic()

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        game.update(dt)
        if not game.player.alive:
            pygame.mixer.music.stop()
            game.level.music_playing = False
            seconds = now - game.start
            game = showgameover(assets, screen, seconds, game.lvl)
        if game.level.game_won:
            pygame.mixer.music.stop()
            pygame.mixer.stop()
            assets.victory_sound.play()
            game.level.music_playting = False
            seconds = now - game.start
            game = showgamewon(assets, screen, seconds, game.lvl)
        screen.fill("black")


        # TUTORIAL FOR LEVEL 1 ------------------------------------------ #
        if game.lvl == 1:
            if now - game.level.initial_message.start <= 5 and now - game.level.initial_message.start >= 0:
                game.level.initial_message.render(screen)
            if now - game.level.initial_message.start <= 10 and now - game.level.initial_message.start >= 5:
                game.level.initial_message.render1(screen)
            if now - game.level.initial_message.start <= 15 and now - game.level.initial_message.start >= 10:
                game.level.initial_message.render2(screen)
            if now - game.level.initial_message.start <= 20 and now - game.level.initial_message.start >= 15:
                game.level.initial_message.render3(screen)
            if now - game.level.initial_message.start <= 23 and now - game.level.initial_message.start >= 20:
                game.level.initial_message.render4(screen)
            if now - game.level.initial_message.start <= 30 and now - game.level.initial_message.start >= 25:
                game.level.initial_message.render5(screen)
            if now - game.level.initial_message.start <= 35 and now - game.level.initial_message.start >= 30:
                game.level.initial_message.render6(screen)
            if now - game.level.initial_message.start <= 40 and now - game.level.initial_message.start >= 35:
                game.level.initial_message.render7(screen)
            if now - game.level.initial_message.start <= 45 and now - game.level.initial_message.start >= 40:
                game.level.initial_message.render7_2(screen)
            if now - game.level.initial_message.start <= 65 and now - game.level.initial_message.start >= 62:
                game.level.initial_message.render8(screen)
            if now - game.level.initial_message.start <= 65 and now - game.level.initial_message.start >= 63:
                game.level.initial_message.render9(screen)
            if now - game.level.initial_message.start <= 80 and now - game.level.initial_message.start >= 75:
                game.level.initial_message.render10(screen)
            if now - game.level.initial_message.start <= 86 and now - game.level.initial_message.start >= 82:
                game.level.initial_message.render11(screen)
            if now - game.level.initial_message.start <= 92 and now - game.level.initial_message.start >= 87:
                game.level.initial_message.render12(screen)
            if now - game.level.initial_message.start <= 97 and now - game.level.initial_message.start >= 92:
                game.level.initial_message.render13(screen)
            if game.level.check5:
                if not game.level.ouch_start_time_defined:
                    ouch_start_time = now
                    game.level.ouch_start_time_defined = True
                if now - ouch_start_time <= 5:
                    game.level.initial_message.renderouch(screen)
                if now - ouch_start_time <= 37 and now - ouch_start_time >= 6:
                    game.level.initial_message.render14(screen)
                if now - ouch_start_time <= 47 and now - ouch_start_time >= 42:
                    game.level.initial_message.render15(screen)
            # if now - game.level.initial_message.start <= 110 and now - game.level.initial_message.start >= 78:
            #     game.level.initial_message.render14(screen)
            # if now - game.level.initial_message.start <= 120 and now - game.level.initial_message.start >= 115:
            #     game.level.initial_message.render15(screen)
        # DIALOGUES-FOR-LEVEL-2------------------------------------------ #
        if game.lvl == 2:
            if now - game.level.dialogue.start <= 5 and now - game.level.dialogue.start >= 0:
                game.level.dialogue.render(screen)
            if now - game.level.dialogue.start <= 12 and now - game.level.dialogue.start >= 10:
                game.level.dialogue.render2(screen)




        game.sprites.draw(screen)
        game.player_sprite.draw(screen)

        # hitboxes -------------------------------------------------------- #
        pygame.draw.rect(screen, (0, 255, 0), game.player.rect_hitbox)
        for shot in game.warning_bubbles:
            pygame.draw.rect(screen, (255, 255, 0), shot.rect_hitbox)
        for shot in game.bubble_shots:
            pygame.draw.rect(screen, (255, 0, 0), shot.rect_hitbox)
        for shot in game.arrow_shots:
            pygame.draw.rect(screen, (255, 0, 0), shot.rect_hitbox)
        for shot in game.chasing_shots:
            pygame.draw.rect(screen, (255, 0, 0), shot.rect_hitbox)
        for enemy in game.enemies:
            pygame.draw.rect(screen, (255, 0, 0), enemy.rect_hitbox)
        for shot in game.shock_shots:
            pygame.draw.rect(screen, (255, 0, 0), shot.rect_hitbox)
        for boss in game.bosses:
            pygame.draw.rect(screen, (255, 0, 0), boss.rect_hitbox)
        # ----------------------------------------------------------------- #

            
        game.fps_counter.render(screen, now, fps)
        game.hp_counter.render(screen, game.player.hp, game.player.max_hp)
        
        for particle in game.particles:
            particle.update(screen)
            if particle.timer <= 0:
                game.particles.remove(particle)

        for particle in game.portal_particles:
            particle.update(dt, screen)
            if particle.timer <= 0:
                game.portal_particles.remove(particle)
        pygame.display.flip()