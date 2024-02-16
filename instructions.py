import pygame
import time
class Instructions:
    def __init__(self, assets):
        self.start = time.monotonic()
        self.font = assets.font
        # self.display_interval = 0.1
        # self.display_timer = 0

    # def display_animation(self, screen, string, color, textpos):
    #     message = ' '
    #     for i in range(len(string)):
    #         if self.display_timer >= self.display_interval:
    #             message += string[i]
    #             text = self.font.render(message, True, color)
    #             text_rect = text.get_rect()
    #             text_rect.center = (textpos.x + 300, textpos.y)
    #             screen.blit(text, text_rect)
    #             self.display_timer = 0
            

    def render(self, screen):
        text = self.font.render("Oh, hello there", True, "white")
        textpos = text.get_rect(centerx=200, centery=screen.get_height()/2-100)
        text2 = self.font.render("my name is Snomin", True, "white")
        textpos2 = text2.get_rect(centerx=200, centery=screen.get_height()/2+100)
        text3 = self.font.render("and i'll be your guide", True, "white")
        textpos3 = text3.get_rect(centerx=200, centery=screen.get_height()/2+150)
        screen.blit(text, textpos)
        screen.blit(text2, textpos2)
        screen.blit(text3, textpos3)

    def render1(self, screen):
        text2 = self.font.render("You may want to use WASD", True, "white")
        textpos2 = text2.get_rect(centerx=200, centery=screen.get_height()/2-150)
        text3 = self.font.render("(or arrow keys) to move.", True, "white")
        textpos3 = text3.get_rect(centerx=200, centery=screen.get_height()/2-100)
        text4 = self.font.render("Your main goal is to dodge", True, "white")
        textpos4 = text4.get_rect(centerx=200, centery=screen.get_height()/2+100)
        text5 = self.font.render("and, of course, survive", True, "white")
        textpos5 = text5.get_rect(centerx=200, centery=screen.get_height()/2+150)
        # textby = "Oh, hello there"
        # self.display_animation(screen, textby, "white", textpos)
        screen.blit(text2, textpos2)
        screen.blit(text3, textpos3)
        screen.blit(text4, textpos4)
        screen.blit(text5, textpos5)

    def render2(self, screen):
        text = self.font.render("This shows your SU score!", True, "white")
        textpos = pygame.Vector2(30, 80)
        text2 = self.font.render("<--", True, "white")
        textpos2 = pygame.Vector2(140, 45)
        text3 = self.font.render("This is your health bar!", True, "green")
        textpos3 = text3.get_rect(centerx=1400, centery=400)
        screen.blit(text, textpos)
        screen.blit(text2, textpos2)
        screen.blit(text3, textpos3)

    def render3(self, screen):
        text = self.font.render("there are walls of shots", True, "white")
        textpos = text.get_rect(centerx=200, centery=screen.get_height()/2-150)
        text2 = self.font.render("coming from the sides!", True, "white")
        textpos2 = text2.get_rect(centerx=200, centery=screen.get_height()/2-100)
        text3 = self.font.render("watch out!", True, "white")
        textpos3 = text3.get_rect(centerx=200, centery=screen.get_height()/2 + 100)
        screen.blit(text, textpos)
        screen.blit(text2, textpos2)
        screen.blit(text3, textpos3)

    def render4(self, screen):
        text = self.font.render("wow, i'm surprised you...", True, "white")
        textpos = text.get_rect(centerx=200, centery=screen.get_height()/2-100)
        text2 = self.font.render("survived my... trial.", True, "red")
        textpos2 = text2.get_rect(centerx=200, centery=screen.get_height()/2+100)
        screen.blit(text, textpos)
        screen.blit(text2, textpos2)
    
    def render5(self, screen):
        text = self.font.render("I just hope you are ready for more.", True, "red")
        textpos = text.get_rect(centerx=screen.get_width()/2, centery=screen.get_height()/2-100)
        screen.blit(text, textpos)

    def render6(self, screen):
        text = self.font.render("so, this is the bubble", True, "white")
        textpos = text.get_rect(centerx=screen.get_width()/2, centery=screen.get_height()/2-100)
        text2 = self.font.render("it takes a while to materialize", True, "white")
        textpos2 = text2.get_rect(centerx=screen.get_width()/2, centery=screen.get_height()/2+100)
        screen.blit(text, textpos)
        screen.blit(text2, textpos2)

    def render7(self, screen):
        text = self.font.render("but when it does... it does", True, "white")
        textpos = text.get_rect(centerx=screen.get_width()/2, centery=screen.get_height()/2-100)
        text2 = self.font.render("damage!", True, "red")
        textpos2 = text2.get_rect(centerx=screen.get_width()/2, centery=screen.get_height()/2+100)
        screen.blit(text, textpos)
        screen.blit(text2, textpos2)

    def render7_2(self, screen):
        text = self.font.render("now... survive this!", True, "white")
        textpos = text.get_rect(centerx=screen.get_width()/2, centery = screen.get_height()/2-100)
        screen.blit(text, textpos)

    def render8(self, screen):
        text = self.font.render("you're very good at dodging...", True, "red")
        textpos = text.get_rect(centerx=screen.get_width()/2, centery=screen.get_height()/2 - 100)
        screen.blit(text, textpos)

    def render9(self, screen):
        text = self.font.render("aren't you?", True, "red")
        textpos = text.get_rect(centerx=screen.get_width()/2, centery=screen.get_height()/2 + 100)
        screen.blit(text, textpos)

    def render10(self, screen):
        text = self.font.render("you don't look like any", True, "white")
        textpos = text.get_rect(centerx=screen.get_width()/2, centery = 250)    
        text2 = self.font.render("of the other ones i've seen...!", True, "white")
        textpos2 = text2.get_rect(centerx = screen.get_width()/2, centery = 300)
        screen.blit(text, textpos)
        screen.blit(text2, textpos2)

    def render11(self, screen):
        text = self.font.render("since you're so promising, i'll teach you", True, "white")
        textpos = text.get_rect(centerx = screen.get_width()/2, centery = 250)
        text2 = self.font.render("one last thing!", True, "white")
        textpos2 = text2.get_rect(centerx = screen.get_width()/2, centery = 300)
        text3 = self.font.render("isn't that exciting?!", True, "white")
        textpos3 = text3.get_rect(centerx= screen.get_width()/2, centery = 350)
        screen.blit(text, textpos)
        screen.blit(text2, textpos2)
        screen.blit(text3, textpos3)

    def render12(self, screen):
        text = self.font.render("well, this is the aiming shot!", True, "white")
        textpos = text.get_rect(centerx=screen.get_width()/2, centery = 250)
        text2 = self.font.render("it aims at things!", True, "white")
        textpos2 = text2.get_rect(centerx=screen.get_width()/2, centery=300)
        screen.blit(text, textpos)
        screen.blit(text2, textpos2)

    def render13(self, screen):
        text = self.font.render("oh, what the shot is aiming at?", True, "white")
        textpos = text.get_rect(centerx=screen.get_width()/2, centery=250)
        text2 = self.font.render("don't worry about that", True, "white")
        textpos2 = text2.get_rect(centerx=screen.get_width()/2, centery=300)
        text3 = self.font.render("it would be really bad if", True, "white")
        textpos3 = text3.get_rect(centerx=screen.get_width()/2, centery=350)
        text4 = self.font.render("it hit me, though", True, "white")
        textpos4 = text4.get_rect(centerx=screen.get_width()/2, centery = 400)        
        screen.blit(text, textpos)
        screen.blit(text2, textpos2)
        screen.blit(text3, textpos3)
        screen.blit(text4, textpos4)

    def render14(self, screen):
        text = self.font.render("you are starting to annoy me.", True, "white")
        textpos = text.get_rect(centerx=screen.get_width()/2, centery=150)
        screen.blit(text, textpos)

    def render15(self, screen):
        text = self.font.render("i'm done with you.", True, "white")
        textpos = text.get_rect(centerx=screen.get_width()/2, centery=150)
        screen.blit(text, textpos)
    
    def renderouch(self, screen):
        text = self.font.render("OUCH!!!", True, "white")
        textpos = text.get_rect(centerx=screen.get_width()/2, centery=150)
        screen.blit(text, textpos)
        