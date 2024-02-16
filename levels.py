import pygame, time, random
from instructions import Instructions
from robox_dialogues import Dialogues
from snomin import Snomin
from snomin_hands import UpHand, DownHand
from portal import Portal
from all_particles import ParticleExplosion
from robox import Robox
class Level0:
    def __init__(self, game, assets):
        self.game = game
        self.assets = assets
        self.speed = 6 * 45
        self.hp = 350
        self.max_hp = 350
        self.vitality = 4
        self.spitter_lifetime = 60
        self.spitter_speed = 0.5 * 45
        self.spitter_spawn_timer = 0
        self.spitter_spawn_interval = 3
        self.warning_lifetime = 3
        self.snomin_lifetime = 9999
        self.snomin_speed = 5
        self.snomin = Snomin(pygame.Vector2(-100, 480), self.snomin_lifetime, self.game, self.assets)
        self.game.bosses.add(self.snomin)
        self.game.player_sprite.add(self.snomin)
        self.initial_message = Instructions(self.assets)
        self.snomin_hands = pygame.sprite.Group()
        # tiros ------------------------- #
        self.bubble_timer = 0
        self.bubble_interval = 0.25
        self.arrow_timer = 0
        self.arrow_interval = 1.25
        self.aiming_timer = 0
        self.aiming_interval = 10
        self.enemy_melee_timer = 0
        self.enemy_melee_interval = 0.2
        # ------------------------------- #
        self.arrow_speed = 4 * 45
        self.chasing_shot_speed = 8 * 45
        self.arrow_damage = 50
        self.bubble_damage = 75
        self.chasing_shot_damage = 100
        self.enemy_melee_damage = 30
        self.start = time.monotonic()
        self.music_playing = False
        pygame.mixer.music.load(assets.tutorial_music_filepath)
        self.stop_sound = assets.stop_sound
        self.check1 = False
        self.check2 = False
        self.check3 = False
        self.check4 = False
        self.check5 = False
        self.check6 = False
        self.check7 = False
        self.check_sound1 = False
        self.check_sound2 = False
        self.check_sound3 = False
        self.check_sound4 = False
        self.check_sound5 = False
        self.snomin_check1 = False
        self.snomin_check2 = False
        self.snomin_check3 = False
        self.snomin_check4 = False
        self.snomin_check5 = False
        self.check_aim = False
        self.ouch_start_time_defined = False
        self.timer = 0
        self.next_pos = pygame.Vector2(0, 0)
        self.game_won = False
        self.switch = False


    def update(self, dt):
        now = time.monotonic()
        # self.initial_message.display_timer += dt
        self.enemy_melee_timer += dt
        self.bubble_timer += dt
        self.arrow_timer += dt
        self.aiming_timer += dt

        if self.music_playing == False:
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.5)
            self.music_playing = True

        for chasing_shot in self.game.chasing_shots:
            chasing_shot.update(dt)
            if pygame.sprite.spritecollide(chasing_shot, self.game.blackwalls, False):
                chasing_shot.kill()
            if pygame.Rect.colliderect(chasing_shot.rect_hitbox, self.game.player.rect_hitbox):
                chasing_shot.kill()
                self.game.player.reduce_hp(self.game, self.chasing_shot_damage)
            
            try:
                if pygame.Rect.colliderect(chasing_shot.rect_hitbox, self.snomin.rect_hitbox):
                    self.check5 = True
                    chasing_shot.kill()
                    for i in range(50):
                        particle = ParticleExplosion(pygame.Vector2(self.snomin.rect.centerx, self.snomin.rect.centery), pygame.color.Color(255, 255, 255))
                        self.game.particles.append(particle)
            except:
                pass
        
        for arrow_shot in self.game.arrow_shots:
            arrow_shot.update(dt)
            if pygame.sprite.spritecollide(arrow_shot, self.game.blackwalls, False):
                arrow_shot.kill()
            if pygame.Rect.colliderect(arrow_shot.rect_hitbox, self.game.player.rect_hitbox):
                arrow_shot.kill()
                self.game.player.reduce_hp(self.game, self.arrow_damage)

        for bubble_shot in self.game.warning_bubbles:
            bubble_shot.update(time.monotonic())

        for bubble_shot in self.game.bubble_shots:
            bubble_shot.update(self.game, time.monotonic())
            if pygame.Rect.colliderect(bubble_shot.rect_hitbox, self.game.player.rect_hitbox):
                bubble_shot.kill()
                self.game.player.reduce_hp(self.game, self.bubble_damage)

        for aiming_shot in self.game.aiming_shots:
            aiming_shot.update(self.game.player.rect.center, time.monotonic())

        if not self.snomin_check1:
            self.next_pos = pygame.Vector2(200, 480)
            self.snomin_check1 = True

        #paredes
        if now - self.start >= 15 and not self.check1:            
            for i in range(220, 851, 70):
                self.game.create_arrow(540, i, pygame.Vector2(1, 0), self.arrow_speed, self.assets)

            for i in range(255, 816, 70):
                self.game.create_arrow(1180, i, pygame.Vector2(-1, 0), self.arrow_speed, self.assets)
            pygame.mixer.music.pause()
            self.stop_sound.play()
            self.check1 = True

        if now - self.start >= 30 and not self.check_sound1:
            pygame.mixer.music.unpause()
            self.check_sound1 = True

        if now - self.start >= 23 and not self.snomin_check2:
            self.next_pos = pygame.Vector2(860, 480)
            for i in range(2, 6):
                self.snomin.grow(i)
            self.snomin_check2 = True

        #bolha demo
        if now - self.start >= 30 and not self.check2:
            self.game.create_bubble(960, 480, 5, 5, self.game, self.assets)
            hand = UpHand(pygame.Vector2(950, 430), 7, self.assets)
            self.snomin_hands.add(hand)
            self.game.sprites.add(hand)
            hand = DownHand(pygame.Vector2(950, 530), 7, self.assets)
            self.snomin_hands.add(hand)
            self.game.sprites.add(hand)
            self.check2 = True

        # bolhas trial
        if now - self.start >= 42 and now - self.start <= 57:
            if self.arrow_timer >= self.arrow_interval:
                if self.switch == False:
                    for i in range(-100, 900, 100):
                        self.game.create_arrow(450, i, pygame.Vector2(2, 1), self.arrow_speed, self.assets)
                    self.switch = True
                else:
                    for i in range(-150, 850, 100):
                        self.game.create_arrow(450, i, pygame.Vector2(2, 1), self.arrow_speed, self.assets)
                    self.switch = False
                self.arrow_timer = 0
            if self.bubble_timer >= self.bubble_interval:
                bubble_x = random.uniform(590, 1160)
                bubble_y = random.uniform(210, 830)
                self.game.create_bubble(bubble_x, bubble_y, 2, 2, self.game, self.assets)
                self.game.create_bubble(self.game.player.rect.centerx + random.uniform(-50, 50), self.game.player.rect.centery + random.uniform(-50, 50), 2, 2, self.game, self.assets)
                self.bubble_timer = 0


        if now - self.start >= 62 and not self.check_sound2:
            pygame.mixer.music.pause()
            self.check_sound2 = True

        #bolhas
        if now - self.start >= 65 and not self.check3:
            self.next_pos = pygame.Vector2(860, 100)
            coords = pygame.Vector2(590, 210)
            while coords.x <= 1160 and coords.y <= 880:
                self.game.create_bubble(coords.x, coords.y, 5, 5, self.game, self.assets)
                coords.x += 50
                if coords.x >= 1160:
                    coords.x = 590
                    coords.y += 50
            for i in range(615, 1116, 50):
                self.game.create_arrow(i, -10, pygame.Vector2(0, 1), self.arrow_speed, self.assets)
            for i in range(235, 880, 50):
                self.game.create_arrow(540, i, pygame.Vector2(1, 0), self.arrow_speed, self.assets)
            self.check3 = True
        if now - self.start >= 73 and not self.check4:
            for i in range(220, 851, 70):
                self.game.create_arrow(540, i, pygame.Vector2(1, 0), self.arrow_speed, self.assets)

            for i in range(260, 821, 70):
                self.game.create_arrow(1180, i, pygame.Vector2(-1, 0), self.arrow_speed, self.assets)
            self.check4 = True
        
        if now-self.start >= 65 and not self.check_sound3:
            pygame.mixer.music.unpause()
            self.stop_sound.play()
            self.check_sound3 = True

        # if now - self.start >= 65 and not self.check5:
        #     for i in range(440, 521, 40):
        #         for j in range(620, 1136, 35):
        #             self.game.create_aiming(j, i, self.game.player.rect.center, 10, self.chasing_shot_speed + 4 * 45)
        #     self.check5 = True
        
        if now - self.start >= 87 and not self.check5 and self.aiming_timer >= self.aiming_interval:
            if self.check_aim == False:
                self.game.create_aiming(860, 480, self.game.player.rect.center, self.aiming_interval, self.chasing_shot_speed + 4 * 45)
                self.check_aim = True
            else:
                if self.aiming_interval == 10:
                    self.aiming_interval = 3.5
                self.game.create_aiming(860, 480, self.game.player.rect.center, self.aiming_interval, self.chasing_shot_speed + 4 * 45)
            self.aiming_timer = 0
            
        if self.check5 and not self.check6:
            self.timer = now
            self.check6 = True

        if now - self.timer <= 1 and not self.check_sound4:
            pygame.mixer.music.pause()
            self.stop_sound.play()
            self.check_sound4 = True
        
        if now - self.timer <= 6 and now - self.timer >= 5 and not self.check_sound5:
            pygame.mixer.music.unpause()
            # self.stop_sound.play()
            self.check_sound5 = True

        # fase final (adicionar chasing shots) ------------------------------------------------------ #
        if now - self.timer >= 7 and now - self.timer <= 37 and self.arrow_timer >= self.arrow_interval and self.check5:
            for i in range(220, 851, 70):
                self.game.create_arrow(540, i, pygame.Vector2(1, 0), self.arrow_speed, self.assets)
            for i in range(255, 816, 70):
                self.game.create_arrow(1180, i, pygame.Vector2(-1, 0), self.arrow_speed, self.assets)
            self.arrow_timer = 0
        if now - self.timer >= 7 and now - self.timer <= 37 and self.bubble_timer >= self.bubble_interval and self.check5:
            bubble_x = random.uniform(590, 1160)
            bubble_y = random.uniform(210, 830)
            self.game.create_bubble(bubble_x, bubble_y, 1, 5, self.game, self.assets)
            self.bubble_timer = 0
        if now - self.timer >= 7 and now - self.timer <= 37 and self.aiming_timer >= self.aiming_interval and self.check5:
            self.game.create_aiming(860, 520, self.game.player.rect.center, self.aiming_interval, self.chasing_shot_speed)
            self.aiming_timer = 0
        # ------------------------------------------------------------------------------------------- #
            
        if now - self.timer >= 42 and now - self.timer <= 43 and self.check5 and not self.snomin_check3:
            self.next_pos = pygame.Vector2(860, -150)
            self.snomin_speed = 0.2
            self.snomin_check3 = True

        if now - self.timer >= 46 and now - self.timer <= 47 and self.check5 and not self.check7:
            self.portal = Portal(pygame.Vector2(860, 480), self.game, self.assets)
            self.game.sprites.add(self.portal)
            self.game.portal.add(self.portal)
            self.check7 = True

        # if not self.check7:
        #     self.portal = Portal(pygame.Vector2(960, 480), self.game, self.assets)
        #     self.game.sprites.add(self.portal)
        #     self.game.portal.add(self.portal)
        #     self.check7 = True
        if len(self.game.portal) != 0:
            for portal in self.game.portal:
                portal.update(dt)
                if pygame.Rect.colliderect(self.game.player.rect_hitbox, portal.rect_hitbox):
                    self.game_won = True

        if len(self.game.bosses) != 0:
            for boss in self.game.bosses:
                boss.update(self.next_pos, dt, now, self.snomin_speed)
            if pygame.Rect.colliderect(self.game.player.rect_hitbox, boss.rect_hitbox) and self.enemy_melee_timer >= self.enemy_melee_interval:
                self.game.player.reduce_hp(self.game, self.enemy_melee_damage)
                self.enemy_melee_timer = 0
        if len(self.snomin_hands) != 0:
            for hand in self.snomin_hands:
                hand.update(dt)
        
class Level1:
    def __init__(self, game, assets):
        self.game = game
        self.assets = assets
        self.speed = 6 * 45
        self.hp = 100 * 1000
        self.max_hp = 100 * 1000
        self.vitality = 4
        self.dialogue = Dialogues(self.assets)
        # tiros ---------------------------- #
        self.bubble_timer = 0
        self.bubble_interval = 0.25
        self.arrow_timer = -5
        self.arrow_interval = 2
        self.aiming_timer = 0
        self.aiming_interval = 10
        self.enemy_melee_timer = 0
        self.enemy_melee_interval = 0.2
        self.arrow_speed = 4 * 45
        self.arrow_damage = 50
        self.enemy_melee_damage = 50
        self.switch = False
        self.enemy_speed = 3 * 45
        self.enemy_lifetime = 25
        self.warning_lifetime = 2
        self.enemy_shot_interval = 1.5
        self.enemy_shot_speed = 3 * 45
        self.enemy_type = 1
        self.shock_damage = 50
        self.shock_timer = 0
        self.shock_interval = 0.5
        self.shock_speed = 3 * 45
        # ---------------------------------- #
        self.robox_lifetime = 9999
        self.robox_speed = 2
        self.next_pos = pygame.Vector2(860, -100)
        self.robox = Robox(pygame.Vector2(860, -100), self.robox_lifetime, self.game, self.assets)
        self.game.bosses.add(self.robox)
        self.game.player_sprite.add(self.robox)
        self.start = time.monotonic()
        self.game_won = False
        self.spawn_check = False
        self.warning_check = False
        self.music_playing = False
        pygame.mixer.music.load(assets.level_1_music_filepath)
        self.checkportal = False
        self.robox_check1 = False


    def update(self, dt):
        now = time.monotonic()
        self.enemy_melee_timer += dt
        self.bubble_timer += dt
        self.arrow_timer += dt
        self.aiming_timer += dt        
        self.shock_timer += dt

        # updates -------------------------------------------- #
        if self.music_playing == False:
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(1)
            self.music_playing = True

        for warning_sign in self.game.warning_signs:
            warning_sign.update(now)

        for arrow_shot in self.game.arrow_shots:
            arrow_shot.update(dt)
            if pygame.sprite.spritecollide(arrow_shot, self.game.blackwalls, False):
                arrow_shot.kill()
            if pygame.Rect.colliderect(arrow_shot.rect_hitbox, self.game.player.rect_hitbox):
                arrow_shot.kill()
                self.game.player.reduce_hp(self.game, self.arrow_damage)

        for shock_shot in self.game.shock_shots:
            shock_shot.update(dt)
            if pygame.sprite.spritecollide(shock_shot, self.game.blackwalls, False):
                shock_shot.kill()
            if pygame.Rect.colliderect(shock_shot.rect_hitbox, self.game.player.rect_hitbox):
                shock_shot.kill()
                self.game.player.reduce_hp(self.game, self.shock_damage)

        if len(self.game.enemies) != 0:
            for enemy in self.game.enemies:
                enemy.update(self.game.player, dt, time.monotonic())
                if pygame.Rect.colliderect(self.game.player.rect_hitbox, enemy.rect_hitbox) and self.enemy_melee_timer >= self.enemy_melee_interval:
                    self.game.player.reduce_hp(self.game, self.enemy_melee_damage)
                    self.enemy_melee_timer = 0

        if len(self.game.portal) != 0:
            for portal in self.game.portal:
                portal.update(dt)
                if pygame.Rect.colliderect(self.game.player.rect_hitbox, portal.rect_hitbox):
                    self.game_won = True

        if len(self.game.bosses) != 0:
            for boss in self.game.bosses:
                boss.update(self.next_pos, dt, now, self.robox_speed)
            if pygame.Rect.colliderect(self.game.player.rect_hitbox, boss.rect_hitbox) and self.enemy_melee_timer >= self.enemy_melee_interval:
                self.game.player.reduce_hp(self.game, self.enemy_melee_damage)
                self.enemy_melee_timer = 0

        # ---------------------------------------------------- #
        # criar paredes de flechas --------------------------- #
        # if self.arrow_timer >= self.arrow_interval:
        #     if self.switch == False:
        #         for i in range(-100, 900, 100):
        #             self.game.create_arrow(450, i, pygame.Vector2(2, 1), self.arrow_speed, self.assets)
        #             self.game.create_arrow(1270, i, pygame.Vector2(-2, 1), self.arrow_speed, self.assets)
        #         self.switch = True
        #     else:
        #         for i in range(-150, 850, 100):
        #             self.game.create_arrow(450, i, pygame.Vector2(2, 1), self.arrow_speed, self.assets)
        #             self.game.create_arrow(1270, i, pygame.Vector2(-2, 1), self.arrow_speed, self.assets)
        #         self.switch = False
        #     self.arrow_timer = 0

        if not self.robox_check1:
            self.next_pos = pygame.Vector2(860, 100)
            self.robox_check1 = True

        if not self.spawn_check and now - self.start >= 10 and now - self.start <= 11:
            self.game.create_warning(860, 520, self.warning_lifetime, self.enemy_lifetime, 0, self.enemy_shot_interval + 2, self.enemy_shot_speed, 2)
            self.game.create_warning(860, 260, self.warning_lifetime, self.enemy_lifetime, self.enemy_speed * 0.4, self.enemy_shot_interval, self.enemy_shot_speed, self.enemy_type)
            self.game.create_warning(860, 850, self.warning_lifetime, self.enemy_lifetime, self.enemy_speed * 0.25, self.enemy_shot_interval, self.enemy_shot_speed, self.enemy_type)
            # self.game.create_warning(1130, 220, self.warning_lifetime, self.enemy_lifetime, self.enemy_speed * 0.625, self.enemy_shot_interval, self.enemy_shot_speed, self.enemy_type)
            # self.game.create_warning(1130, 850, self.warning_lifetime, self.enemy_lifetime, self.enemy_speed * 0.5, self.enemy_shot_interval, self.enemy_shot_speed, self.enemy_type)          
            self.spawn_check = True

        if now - self.start >= 7 and now - self.start <= 37 and self.shock_timer >= self.shock_interval:
            for i in range(600, 851, 50):
                self.game.create_shock(i, 160, pygame.Vector2(-2, 3), self.shock_speed, self.game.assets)
                self.game.create_shock(i, 900, pygame.Vector2(-2, -3), self.shock_speed, self.game.assets)
            for i in range(850, 1100, 50):
                self.game.create_shock(i, 160, pygame.Vector2(2, 3), self.shock_speed, self.game.assets)
                self.game.create_shock(i, 900, pygame.Vector2(2, -3), self.shock_speed, self.game.assets)
            self.shock_timer = 0

        if not self.warning_check and now - self.start >= 5 and now - self.start <= 6:
            self.game.create_major_warning(650, 280, 5, 4)
            self.game.create_major_warning(650, 780, 5, 4)
            self.game.create_major_warning(1090, 280, 5, 4)
            self.game.create_major_warning(1090, 780, 5, 4)
            self.warning_check = True

        # if now - self.start >= 



        if now - self.start >= 240 and now - self.start <= 241 and not self.checkportal:
            self.portal = Portal(pygame.Vector2(860, 480), self.game, self.assets)
            self.game.sprites.add(self.portal)
            self.game.portal.add(self.portal)
            self.checkportal = True