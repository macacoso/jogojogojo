import pygame
import time
import random

from chasing_shots import ChasingShot
from arrow_shots import ArrowShot
from fps_counter import FpsCounter
from player import Player
from walls import Wall
from warning_bubble import WarningBubble
from spitter import Spitter
from instructions import Instructions
from warning_spawn import WarningSign
from hp_counter import HpCounter
from levels import Level0, Level1
from aiming_shot import AimingShot
from shock_shots import ShockShot
from warning import Warning
class GameState:
    def __init__(self, level, screen, assets):
        self.lvl = level

        # self.speed = 6 * 45
        self.size = 64
        # self.hp = 250
        # self.max_hp = 250
        # self.vitality = 4
        self.sprites = pygame.sprite.Group()
        self.player_sprite = pygame.sprite.Group()      
        self.enemies = pygame.sprite.Group()
        self.bosses = pygame.sprite.Group()
        self.chasing_shots = pygame.sprite.Group()
        self.arrow_shots = pygame.sprite.Group()
        self.shock_shots = pygame.sprite.Group()
        self.warning_bubbles = pygame.sprite.Group()
        self.warning_signs = pygame.sprite.Group()
        self.bubble_shots = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.blackwalls = pygame.sprite.Group()
        self.aiming_shots = pygame.sprite.Group()
        self.portal = pygame.sprite.Group()
        self.portal_particles = []
        self.particles = []
        # self.last_shot = 10
        # self.shot_speed = 3 * 45
        # self.bubble_timer = -1
        self.bubble_interval = 0.5
        self.arrow_timer = -1
        self.arrow_interval = 1.5
        self.chasing_timer = -1
        self.chasing_interval = 1.5
        self.assets = assets
        self.create_walls(screen)
        # spitter_lifetime = 999
        # spitter_speed = 0 * 45
        # self.spitter_spawn_timer = 0
        # self.spitter_spawn_interval = 3
        # self.warning_lifetime = 3
        # self.warning = WarningSign(screen.get_width()/2, screen.get_height()/2, self.warning_lifetime, spitter_lifetime, spitter_speed, self, assets)
        # self.warning_signs.add(self.warning)
        # self.sprites.add(self.warning)
        self.screen = screen
        # self.initial_message = Instructions(assets)
        self.fps_counter = FpsCounter(time.monotonic(), assets)
        self.clock = pygame.time.Clock()
        self.start = time.monotonic()
        self.hp_counter = HpCounter(assets)
        if level == 1:
            self.level = Level0(self, assets)
        elif level == 2:
            self.level = Level1(self, assets)



        self.player = Player(self.size, self.level.speed, self.level.vitality, self.level.hp, self.level.max_hp, screen, assets)
        self.player_sprite.add(self.player)


    def update(self, dt):
        self.level.update(dt)
        # colocar em levels.py -------------------- #
        # self.level.bubble_timer += dt
        # self.level.arrow_timer += dt
        # self.level.chasing_timer += dt
        # self.level.spitter_spawn_timer += dt
        # self.level.spitter_melee_timer += dt
        # ----------------------------------------- #
        #nova bolhha
        # if self.bubble_timer >= self.bubble_interval:
        #     bubble_x = random.uniform(570, 1150)
        #     bubble_y = random.uniform(190, 870)
        #     self.create_bubble(bubble_x, bubble_y, lifetime, bubble_lifetime, self, self.assets)
        #     self.bubble_timer = 0

        #nova flecha
        # if self.arrow_timer >= self.arrow_interval:
        #     self.create_arrow(450, random.uniform(190, 870), pygame.Vector2(1, 0), self.shot_speed, self.assets)
        #     self.create_arrow(1260, random.uniform(190, 870), pygame.Vector2(-1, 0), self.shot_speed, self.assets)
        #     self.create_arrow(random.uniform(570, 1140), 950, pygame.Vector2(0, -1), self.shot_speed, self.assets)
        #     self.create_arrow(random.uniform(570, 1140), 70, pygame.Vector2(0, 1), self.shot_speed, self.assets)
        #     self.arrow_timer = 0
        # if  self.spitter_spawn_timer >= self.spitter_spawn_interval:
        #     for enemy in self.enemies:
        #         enemy.nova16(self.shot_speed, self, self.assets)
        #     self.spitter_spawn_timer = 0

        # if self.chasing_timer >= self.chasing_interval:
        #     self.create_chasing(550, 180, self.player.rect.center, self.shot_speed, self.assets)
        #     self.create_chasing(1160, 880, self.player.rect.center, self.shot_speed, self.assets)
        #     self.chasing_timer = 0

        keys = pygame.key.get_pressed()
        self.player.update(keys, dt)

        # for chasing_shot in self.chasing_shots:
        #     chasing_shot.update(dt)
        #     if pygame.sprite.spritecollide(chasing_shot, self.blackwalls, False):
        #         chasing_shot.kill()
        #     if pygame.Rect.colliderect(chasing_shot.rect_hitbox, self.player.rect_hitbox):
        #         chasing_shot.kill()
        #         self.player.reduce_hp(self, self.level.chasing_shot_damage)
            
        #     try:
        #         if pygame.Rect.colliderect(chasing_shot.rect_hitbox, self.level.snomin.rect_hitbox):
        #             self.level.check5 = True
        #             chasing_shot.kill()
        #             for i in range(50):
        #                 particle = ParticleExplosion(pygame.Vector2(self.level.snomin.rect.centerx, self.level.snomin.rect.centery), pygame.color.Color(255, 255, 255))
        #                 self.particles.append(particle)
        #     except:
        #         pass

        # for arrow_shot in self.arrow_shots:
        #     arrow_shot.update(dt)
        #     if pygame.sprite.spritecollide(arrow_shot, self.blackwalls, False):
        #         arrow_shot.kill()
        #     if pygame.Rect.colliderect(arrow_shot.rect_hitbox, self.player.rect_hitbox):
        #         arrow_shot.kill()
        #         self.player.reduce_hp(self, self.level.arrow_damage)

        # for bubble_shot in self.warning_bubbles:
        #     bubble_shot.update(time.monotonic())

        # for warning_sign in self.warning_signs:
        #     warning_sign.update(self, time.monotonic())

        # for bubble_shot in self.bubble_shots:
        #     bubble_shot.update(self, time.monotonic())
        #     if pygame.Rect.colliderect(bubble_shot.rect_hitbox, self.player.rect_hitbox):
        #         bubble_shot.kill()
        #         self.player.reduce_hp(self, self.level.bubble_damage)
        
        # for aiming_shot in self.aiming_shots:
        #     aiming_shot.update(self.player.rect.center, time.monotonic())

        collisions = pygame.sprite.spritecollide(self.player, self.walls, False)
        if collisions:
            collided_x  = False
            collided_y = False
            for collision in collisions:
                if collision.axis == "x":
                    collided_x = True
                elif collision.axis == "y":
                    collided_y = True
            if collided_x:
                self.player.rect.x = self.player.old_x
            if collided_y:
                self.player.rect.y = self.player.old_y

        # adicionar em niveis e nao em gamestate! --------------- #
        # if len(self.enemies) != 0:
        #     for enemy in self.enemies:
        #         enemy.update(self.player, dt, time.monotonic())
        #         if pygame.Rect.colliderect(self.player.rect_hitbox, enemy.rect_hitbox) and self.level.enemy_melee_timer >= self.level.enemy_melee_interval:
        #             self.player.reduce_hp(self, self.level.enemy_melee_damage)
        #             self.level.enemy_melee_timer = 0
        # ------------------------------------------------------- #


    def create_walls(self, screen):
        #left wall
        wall1 = Wall(560, 180, 10, 700, "white", "x")
        #right wall
        wall2 = Wall(1160, 180, 10, 700, "white", "x")
        #upper wall
        wall3 = Wall(560, 180, 600, 10, "white", "y")
        #"downer" wall
        wall4 = Wall(560, 880, 610, 10, "white", "y")
        blackwall1 = Wall(screen.get_width()/2 - 450, -200, 1, screen.get_height() + 400, "black", "x")
        blackwall2 = Wall(screen.get_width()/2 + 450, -200, 1, screen.get_height() + 400, "black", "x")
        blackwall3 = Wall(screen.get_width()/2 - 450, -200, 900, 1, "black", "y")
        blackwall4 = Wall(screen.get_width()/2 - 450, screen.get_height() + 200, 900, 1, "black", "y")
        
        
        self.sprites.add(wall1, wall2, wall3, wall4)
        self.walls.add(wall1, wall2, wall3, wall4)
        self.blackwalls.add(blackwall1, blackwall2, blackwall3, blackwall4)

    def create_chasing(self, spawn_x, spawn_y, player_pos, shot_speed, assets):
        chasing_shot = ChasingShot(spawn_x, spawn_y, player_pos, shot_speed, self, assets)
        self.chasing_shots.add(chasing_shot)
        self.sprites.add(chasing_shot)

    def create_bubble(self, spawn_x, spawn_y, lifetime, bubble_lifetime, game, assets):
        bubble_shot = WarningBubble(spawn_x, spawn_y, lifetime, bubble_lifetime, game, assets)
        self.warning_bubbles.add(bubble_shot)
        self.sprites.add(bubble_shot)

    def create_arrow(self, spawn_x, spawn_y, direction, shot_speed, assets):
        arrow_shot = ArrowShot(spawn_x, spawn_y, direction, shot_speed, assets)
        self.arrow_shots.add(arrow_shot)
        self.sprites.add(arrow_shot)

    def create_shock(self, spawn_x, spawn_y, direction, shot_speed, assets):
        shock_shot = ShockShot(spawn_x, spawn_y, direction, shot_speed, assets)
        self.shock_shots.add(shock_shot)
        self.sprites.add(shock_shot)

    def create_aiming(self, spawn_x, spawn_y, player_pos, lifetime, shot_speed):
        aiming_shot = AimingShot(spawn_x, spawn_y, player_pos, lifetime, shot_speed, self, self.assets)
        self.aiming_shots.add(aiming_shot)
        self.sprites.add(aiming_shot)

    def create_warning(self, spawn_x, spawn_y, lifetime, spitter_lifetime, spitter_speed, spitter_shot_interval, spitter_shot_speed, spitter_type):
        warning = WarningSign(spawn_x, spawn_y, lifetime, spitter_lifetime, spitter_speed, spitter_shot_interval, spitter_shot_speed, spitter_type, self)
        self.warning_signs.add(warning)
        self.sprites.add(warning)

    def create_major_warning(self, spawn_x, spawn_y, lifetime, size):
        warning = Warning(pygame.Vector2(spawn_x, spawn_y), lifetime, size, self.assets)
        self.warning_signs.add(warning)
        self.sprites.add(warning)