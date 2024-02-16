import pygame

class Assets:
    def __init__(self):
        self.font = pygame.font.SysFont("Arial", 30)
        # self.char = pygame.image.load("assets/sprites/player.png")
        # self.tutorial_music_filepath = "assets/music/tutorial music.wav"
        # self.chasing_shot = pygame.image.load("assets/sprites/icicle2.png")
        # self.arrow_shot = pygame.image.load("assets/sprites/ice arrow.png")
        # self.bubble_shot = pygame.image.load("assets/sprites/ice bubble.png")
        # self.bubble_warning = pygame.image.load("assets/sprites/ice bubble warning.png")
        # self.spitter = pygame.image.load("assets/sprites/spitter.png")
        # self.warning_sign = pygame.image.load("assets/sprites/warning.png")
        # self.damage_sound = pygame.mixer.Sound("assets/sounds/damage.wav")
        # self.stop_sound = pygame.mixer.Sound("assets/sounds/stop.mp3")
        # self.snomin = pygame.image.load("assets/sprites/snomin.png")
        # self.snomin_hand_up = pygame.image.load("assets/sprites/snomin hand up.png")
        # self.snomin_hand_down = pygame.image.load("assets/sprites/snomin hand down.png")
        self.char = pygame.image.load("violino/assets/sprites/player.png")
        self.tutorial_music_filepath = "violino/assets/music/tutorial music.wav"
        self.level_1_music_filepath = "violino/assets/music/level 1 music.wav"
        self.chasing_shot = pygame.image.load("violino/assets/sprites/icicle2.png")
        self.arrow_shot = pygame.image.load("violino/assets/sprites/ice arrow.png")
        self.bubble_shot = pygame.image.load("violino/assets/sprites/ice bubble.png")
        self.bubble_warning = pygame.image.load("violino/assets/sprites/ice bubble warning.png")
        self.spitter = pygame.image.load("violino/assets/sprites/spitter.png")
        self.warning_sign = pygame.image.load("violino/assets/sprites/warning.png")
        self.damage_sound = pygame.mixer.Sound("violino/assets/sounds/damage.wav")
        self.stop_sound = pygame.mixer.Sound("violino/assets/sounds/stop.mp3")
        self.snomin = pygame.image.load("violino/assets/sprites/snomin.png")
        self.snomin_hand_up = pygame.image.load("violino/assets/sprites/snomin hand up.png")
        self.snomin_hand_down = pygame.image.load("violino/assets/sprites/snomin hand down.png")
        self.victory_sound = pygame.mixer.Sound("violino/assets/sounds/yippee.mp3")
        self.portal = pygame.image.load("violino/assets/sprites/portal.png")
        self.portal_activate = pygame.mixer.Sound("violino/assets/sounds/portal activate.wav")
        self.shock_shot = pygame.image.load("violino/assets/sprites/shock shot.png")
        self.robox = pygame.image.load("violino/assets/sprites/robox.png")