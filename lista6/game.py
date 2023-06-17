import pygame
from sys import exit
from settings import *
from supp import display_text
from level import Level
from button import Button
from ui import UI
import json
import os


pygame.init()


#Variables
FPS = 60
running = True

#Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font1 = pygame.font.Font("semestr2\\lista6\\font\\Pixeltype.ttf", 200)
font2 = pygame.font.Font("semestr2\\lista6\\font\\Pixeltype.ttf", 100)
you_died = font1.render("YOU DIED", False, (162,11,11))
you_died_rect = you_died.get_rect(center = (WIDTH/2, HEIGHT/2-50))
press_space = font2.render("PRESS SPACE TO CONTINUE", False, (255,255,255))
press_space_rect = press_space.get_rect(center = (WIDTH/2, HEIGHT/2+200))
pygame.display.set_caption("My game")
clock = pygame.time.Clock()

#Menu
blank_button_img = pygame.image.load("semestr2\\lista6\\graphics\\menu\\blank_button.png").convert_alpha()
new_game_button = Button((WIDTH/2, 100), blank_button_img, 1, "NEW GAME")
score_button = Button((WIDTH/2, 200), blank_button_img, 1, "SCORE")
rules_button = Button((WIDTH/2,300), blank_button_img, 1, "RULES")
about_button = Button((WIDTH/2,400), blank_button_img, 1, "ABOUT")
quit_button = Button((WIDTH/2,500), blank_button_img, 1, "QUIT")
resume_button = Button((WIDTH/2,HEIGHT/2), blank_button_img, 1, "RESUME")
back_button = Button((WIDTH/2,600), blank_button_img, 1, "BACK")



class GameState():
    def __init__(self):
        self.state = "main_menu"
        self.is_paused = False
        self.ui = UI(screen)
        self.level_number = 0
        self.load_highscores()
        self.score = 0
        self.health = 3
        
    def main_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()         
                exit()
        
        screen.fill("grey")
        if new_game_button.draw(screen):
            self.level_number = 0
            self.score = 0
            self.level = Level(levels[self.level_number], screen)
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
            self.health = self.level.get_player_health()
            self.current_score = self.level.get_player_score()
            self.ui.show_score(self.current_score)
            self.ui.show_health(self.health)
            self.check_death()
            self.check_win()


    def next_level(self):
        self.level = Level(levels[self.level_number], screen)
        self.state = "main_game"


    def game_over(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.state = "main_menu"
            if event.type == pygame.QUIT:
                pygame.quit()         
                exit()

        screen.fill("black")
        screen.blit(you_died, you_died_rect)
        screen.blit(press_space, press_space_rect)


    def score_(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()         
                exit()
        
        screen.fill("grey")
        self.display_highscores()
        if back_button.draw(screen):
            self.state = "main_menu"


    def rules(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()         
                exit()
        
        screen.fill("grey")
        self.display_rules()
        if back_button.draw(screen):
            self.state = "main_menu"


    def about(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()         
                exit()
        
        screen.fill("grey")
        self.display_about()
        if back_button.draw(screen):
            self.state = "main_menu"


    def paused(self):
        screen.fill("gray")
        if resume_button.draw(screen):
            self.is_paused = False
        elif quit_button.draw(screen):
            self.is_paused = False
            self.state = "main_menu"


    def check_death(self):
        if self.health <= 0:
            self.score += self.current_score
            self.add_new_highscore(self.score)
            self.save_highscores()
            self.state = "game_over"

    
    def check_win(self):
        if self.level.goal_collision():
            self.level_number += 1
            if self.level_number <= 2:
                self.score += self.current_score
                self.state = "next_level"
            else:
                self.score += self.current_score
                self.add_new_highscore(self.score)
                self.save_highscores()
                self.state = "main_menu"
                self.level_number = 0

    
    def load_highscores(self):
        if os.path.exists("semestr2\lista6\highscores.json"):
            with open("semestr2\lista6\highscores.json") as f:
                self.highscores = json.load(f)
            print(self.highscores)


    def save_highscores(self):
        with open("semestr2\lista6\highscores.json", "w") as f:
            json.dump(self.highscores, f)


    def add_new_highscore(self, score):
        for index, value in enumerate(self.highscores):
            if score > value:
                self.highscores[index] = score
                break


    def display_highscores(self):
        user = os.getlogin()
        caption1 = font2.render(f"1. ({user if self.highscores[0] > 0 else None}): {self.highscores[0]}", False, (255,255,255))
        caption2 = font2.render(f"2. ({user if self.highscores[1] > 0 else None}): {self.highscores[1]}", False, (255,255,255))
        caption3 = font2.render(f"3. ({user if self.highscores[2] > 0 else None}): {self.highscores[2]}", False, (255,255,255))
        caption_rect1 = caption1.get_rect(center = (WIDTH/2, HEIGHT/2-200))
        caption_rect2 = caption1.get_rect(center = (WIDTH/2, HEIGHT/2-100))
        caption_rect3 = caption1.get_rect(center = (WIDTH/2, HEIGHT/2))
        screen.blit(caption1, caption_rect1)
        screen.blit(caption2, caption_rect2)
        screen.blit(caption3, caption_rect3)


    def display_rules(self):
        text = ("Your goal is to beat all levels by picking up a key at the end of every map. Collect coins to get higher score but watch out for enemies.\
                \n \nControls: \nA, D or L_ARROW, R_ARROW to run, \nSPACE to jump, \nESC to pause")
        display_text(screen, text, (20,20), font2, (255,255,255))


    def display_about(self):
        text = ("Game by Hubert Zawerbny \nHave fun ;)")
        display_text(screen, text, (20,20), font2, (255,255,255))


    def get_state(self):
        if self.state == "main_game":
            self.main_game()
        elif self.state == "main_menu":
            self.main_menu()
        elif self.state == "game_over":
            self.game_over()
        elif self.state == "next_level":
            self.next_level()
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
