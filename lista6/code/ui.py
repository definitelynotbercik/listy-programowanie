import pygame

class UI():
    def __init__(self, surface):
        """
        Initializes the UI class.

        Args:
            surface (pygame.Surface): The surface to display the UI on.
        """

        self.display_surface = surface

        self.full_heart = pygame.image.load("semestr2\\lista6\\graphics\\ui\\full_heart.png").convert_alpha()
        self.empty_heart = pygame.image.load("semestr2\\lista6\\graphics\\ui\\empty_heart.png").convert_alpha()
        self.full_heart = pygame.transform.scale(self.full_heart, (30,30)).convert_alpha()
        self.empty_heart = pygame.transform.scale(self.empty_heart, (30,30))

        self.score = pygame.image.load("semestr2\\lista6\\graphics\\coin\\01.png").convert_alpha()
        self.score_rect = self.score.get_rect(topleft = (50,61))
        self.font = pygame.font.Font("semestr2\\lista6\\font\\Pixeltype.ttf", 30)


    def show_health(self, amount):
        """
        Displays the health UI based on the given amount.

        Args:
            amount (int): The health amount (1-3).
        """

        if amount == 3:
            self.display_surface.blit(self.full_heart, (20,10))
            self.display_surface.blit(self.full_heart, (50,10))
            self.display_surface.blit(self.full_heart, (80,10))
        elif amount == 2:
            self.display_surface.blit(self.full_heart, (20,10))
            self.display_surface.blit(self.full_heart, (50,10))
            self.display_surface.blit(self.empty_heart, (80,10))
        elif amount == 1:
            self.display_surface.blit(self.full_heart, (20,10))
            self.display_surface.blit(self.empty_heart, (50,10))
            self.display_surface.blit(self.empty_heart, (80,10))
        else:
            self.display_surface.blit(self.empty_heart, (20,10))
            self.display_surface.blit(self.empty_heart, (50,10))
            self.display_surface.blit(self.empty_heart, (80,10))


    def show_score(self, amount):
        """
        Displays the score UI.

        Args:
            amount (int): The score amount.
        """

        self.display_surface.blit(self.score, self.score_rect)
        score_amount_surface = self.font.render(str(amount), False, "#3A2C2C")
        score_amount_rect = score_amount_surface.get_rect(midleft = (self.score_rect.right + 4, self.score_rect.centery))
        self.display_surface.blit(score_amount_surface, score_amount_rect)
        