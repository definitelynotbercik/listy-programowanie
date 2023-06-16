import pygame
from sys import exit
from settings import *
from level import Level
from button import Button
import player

pygame.init()


#Variables
FPS = 60
running = True

#Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My game")                 
clock = pygame.time.Clock()
#level = Level(levels[0], screen)

#Menu
blank_button_img = pygame.image.load("semestr2\\lista6\\graphics\\menu\\blank_button.png").convert_alpha()
new_game_button = Button((WIDTH/2, 100), blank_button_img, 1, "NEW GAME")
score_button = Button((WIDTH/2, 200), blank_button_img, 1, "SCORE")
rules_button = Button((WIDTH/2,300), blank_button_img, 1, "RULES")
about_button = Button((WIDTH/2,400), blank_button_img, 1, "ABOUT")
quit_button = Button((WIDTH/2,500), blank_button_img, 1, "QUIT")
resume_button = Button((WIDTH/2,HEIGHT/2), blank_button_img, 1, "RESUME")
back_button = Button((666,666), blank_button_img, 1, "BACK")



class GameState():
    def __init__(self):
        self.state = "main_menu"
        self.is_paused = False
        self.score = 0
        
    def main_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()         
                exit()
        
        screen.fill("grey")
        if new_game_button.draw(screen):
            self.level = Level(levels[0], screen)
            self.state = "main_game"
        elif score_button.draw(screen):
            self.state = "score"
        elif rules_button.draw(screen):
            self.state = "rules"
        elif about_button.draw(screen):
            self.state = "about"
        elif quit_button.draw(screen):
            pygame.quit()
            exit()    


    def main_game(self):    
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.is_paused = True
            if event.type == pygame.QUIT:
                pygame.quit()         
                exit()

        if self.is_paused:
            self.paused()
        else:    
            screen.fill("light blue")
            self.level.generate()
            self.score = self.level.get_player_score()
            print(self.score)
        

    def score_(self):
        pass


    def rules(self):
        pass


    def about(self):
        pass


    def paused(self):
        screen.fill("gray")
        if resume_button.draw(screen):
            self.is_paused = False
        elif quit_button.draw(screen):
            self.is_paused = False
            self.state = "main_menu"


    def get_state(self):
        if self.state == "main_game":
            self.main_game()
        elif self.state == "main_menu":
            self.main_menu()
        elif self.state == "score":
            self.score_()
        elif self.state == "rules":
            self.rules()
        elif self.state == "about":
            self.about()


game_state = GameState()


while running:
    game_state.get_state()

    pygame.display.update()
    clock.tick(FPS)

