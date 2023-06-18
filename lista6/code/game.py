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


# Variables
FPS = 60
running = True

# Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
font1 = pygame.font.Font("semestr2\\lista6\\font\\Pixeltype.ttf", 200)
font2 = pygame.font.Font("semestr2\\lista6\\font\\Pixeltype.ttf", 100)
you_died = font1.render("YOU DIED", False, (162,11,11))
you_died_rect = you_died.get_rect(center = (WIDTH/2, HEIGHT/2-50))
press_space = font2.render("PRESS SPACE TO CONTINUE", False, (255,255,255))
press_space_rect = press_space.get_rect(center = (WIDTH/2, HEIGHT/2+200))
pygame.display.set_caption("Pirates and Crabs")
clock = pygame.time.Clock()

# Menu
blank_button_img = pygame.image.load("semestr2\\lista6\\graphics\\menu\\blank_button.png").convert_alpha()
speaker_on_img = pygame.image.load("semestr2\lista6\graphics\menu\speaker_on.png").convert_alpha()
speaker_off_img = pygame.image.load("semestr2\lista6\graphics\menu\speaker_off.png").convert_alpha()
new_game_button = Button((WIDTH/2, 100), blank_button_img, 1, "NEW GAME")
score_button = Button((WIDTH/2, 200), blank_button_img, 1, "SCORE")
rules_button = Button((WIDTH/2,300), blank_button_img, 1, "RULES")
about_button = Button((WIDTH/2,400), blank_button_img, 1, "ABOUT")
quit_button = Button((WIDTH/2,500), blank_button_img, 1, "QUIT")
resume_button = Button((WIDTH/2,HEIGHT/2), blank_button_img, 1, "RESUME")
back_button = Button((WIDTH/2,600), blank_button_img, 1, "BACK")
speaker_on_button = Button((WIDTH/2+500,640), speaker_on_img, 0.2, "")
speaker_off_button = Button((WIDTH/2+500,640), speaker_off_img, 0.2, "")



class GameState():
    def __init__(self):
        """Initialize the GameState object."""

        self.state = "main_menu"
        self.is_paused = False
        self.ui = UI(screen)
        self.level_number = 0
        self.highscores = {}
        self.load_highscores()
        self.score = 0
        self.health = 3

        # Sound
        self.mute_sound = False
        self.menu_sound = pygame.mixer.Sound("semestr2\lista6\sounds\menu.wav")
        self.menu_sound.set_volume(0.1)
        self.game_sound = pygame.mixer.Sound("semestr2\lista6\sounds\game.wav")
        self.game_sound.set_volume(0.1)
        self.game_over_sound = pygame.mixer.Sound("semestr2\lista6\sounds\game_over.wav")
        self.menu_sound.play(loops=-1)
        
    def main_menu(self):
        """Handle the main menu state."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()         
                exit()
        
        screen.fill("grey")
        if new_game_button.draw(screen):
            self.level_number = 0
            self.score = 0
            self.level = Level(levels[self.level_number], screen)
            if not self.mute_sound:
                self.menu_sound.stop()
                self.game_sound.play(loops=-1)
            self.state = "main_game"
        if score_button.draw(screen):
            self.state = "score"
        if rules_button.draw(screen):
            self.state = "rules"
        if about_button.draw(screen):
            self.state = "about"
        if quit_button.draw(screen):
            pygame.quit()
            exit()
        if self.mute_sound == True:
            if speaker_off_button.draw(screen):
                self.menu_sound.play(loops=-1)
                self.mute_sound = False
        else:
            if speaker_on_button.draw(screen):
                self.menu_sound.stop()
                self.mute_sound = True


    def main_game(self):
        """Handle the main game state."""

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
        """Handle the transition to the next level."""

        self.level = Level(levels[self.level_number], screen)
        self.state = "main_game"


    def game_over(self):
        """Handle the game over state."""

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if not self.mute_sound:
                    self.game_over_sound.stop()
                    self.menu_sound.play(loops=-1)
                self.state = "main_menu"
            if event.type == pygame.QUIT:
                pygame.quit()         
                exit()

        screen.fill("black")
        screen.blit(you_died, you_died_rect)
        screen.blit(press_space, press_space_rect)


    def score_(self):
        """Handle the score state."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()         
                exit()
        
        screen.fill("grey")
        self.display_highscores()
        if back_button.draw(screen):
            self.state = "main_menu"


    def rules(self):
        """Handle the rules state."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()         
                exit()
        
        screen.fill("grey")
        self.display_rules()
        if back_button.draw(screen):
            self.state = "main_menu"


    def about(self):
        """Handle the about state."""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()         
                exit()
        
        screen.fill("grey")
        self.display_about()
        if back_button.draw(screen):
            self.state = "main_menu"


    def paused(self):
        """Handle the paused state."""

        screen.fill("gray")
        if resume_button.draw(screen):
            self.is_paused = False
        elif quit_button.draw(screen):
            self.is_paused = False
            if not self.mute_sound:
                self.game_sound.stop()
                self.menu_sound.play(loops=-1)
            self.state = "main_menu"


    def check_death(self):
        """Check if the player's health is zero and transition to the game over state."""

        if self.health <= 0:
            self.score += self.current_score
            self.add_new_highscore(self.score)
            self.save_highscores()
            if not self.mute_sound:
                self.game_sound.stop()
                self.game_over_sound.play(loops=-1)
            self.state = "game_over"

    
    def check_win(self):
        """Check if the player has reached the goal and transition to the next level or main menu state."""

        if self.level.goal_collision():
            self.level_number += 1
            if self.level_number <= 2:
                self.score += self.current_score
                self.state = "next_level"
            else:
                self.score += self.current_score
                self.add_new_highscore(self.score)
                self.save_highscores()
                if not self.mute_sound:
                    self.game_sound.stop()
                    self.menu_sound.play(loops=-1)
                self.state = "main_menu"
                self.level_number = 0

    
    def load_highscores(self):
        """Load the highscores from a JSON file."""

        if os.path.exists("semestr2\lista6\highscores.json"):
            with open("semestr2\lista6\highscores.json") as f:
                self.highscores = json.load(f)


    def save_highscores(self):
        """Save the highscores to a JSON file."""

        with open("semestr2\lista6\highscores.json", "w") as f:
            json.dump(self.highscores, f)


    def add_new_highscore(self, score):
        """Add a new highscore to the dictionary if it's higher than the existing ones."""
        
        user = os.getlogin()

        # Add new highscore
        if user in self.highscores.keys():
            if score > self.highscores[user]:
                self.highscores[user] = score
        else:
            self.highscores[user] = score

        # Sort and delete last item
        self.highscores = dict(sorted(self.highscores.items(), key=lambda x: x[1], reverse=True))
        if len(self.highscores) > 3:
            self.highscores.popitem()


    def display_highscores(self):
        """Display the highscores on the screen."""
        user1 = list(self.highscores)[0]
        user2 = list(self.highscores)[1]
        user3 = list(self.highscores)[2]

        caption1 = font2.render(f"1. ({user1 if self.highscores[user1] > 0 else None}): {self.highscores[user1]}", False, (255,255,255))
        caption2 = font2.render(f"2. ({user2 if self.highscores[user2] > 0 else None}): {self.highscores[user2]}", False, (255,255,255))
        caption3 = font2.render(f"3. ({user3 if self.highscores[user3] > 0 else None}): {self.highscores[user3]}", False, (255,255,255))
        caption_rect1 = caption1.get_rect(center = (WIDTH/2, HEIGHT/2-200))
        caption_rect2 = caption1.get_rect(center = (WIDTH/2, HEIGHT/2-100))
        caption_rect3 = caption1.get_rect(center = (WIDTH/2, HEIGHT/2))
        screen.blit(caption1, caption_rect1)
        screen.blit(caption2, caption_rect2)
        screen.blit(caption3, caption_rect3)


    def display_rules(self):
        """Display the rules on the screen."""

        text = ("Your goal is to beat all levels by picking up a key at the end of every map. Collect coins to get higher score but watch out for enemies.\
                \n \nControls: \nA, D or L_ARROW, R_ARROW to run, \nSPACE to jump, \nESC to pause")
        display_text(screen, text, (20,20), font2, (255,255,255))


    def display_about(self):
        """Display the about information on the screen."""

        text = ("Game by Hubert Zawerbny \nHave fun ;)")
        display_text(screen, text, (20,20), font2, (255,255,255))


    def get_state(self):
        """Based on state attribute display specific game state"""

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

# Run game
while running:
    game_state.get_state()

    pygame.display.update()
    clock.tick(FPS)
