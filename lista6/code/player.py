import pygame
from supp import import_folder
from math import sin

class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        """
        Initialize the Player object.

        Args:
            position (tuple): The initial position of the player (x, y).
        """

        # Main
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations["idle"][self.frame_index]
        self.rect = self.image.get_rect(topleft = position)
        self.score = 0
        self.health = 3
        self.invincible = False
        self.invincibility_duration = 500
        self.hurt_time = 0

        # Sound
        self.damage_sound = pygame.mixer.Sound("semestr2\lista6\sounds\damage.wav")
        self.jump_sound = pygame.mixer.Sound("semestr2\lista6\sounds\jump.wav")
        
        # Movement
        self.movement_direction = pygame.math.Vector2(0,0)
        self.speed = 5
        self.gravity = 0.5
        self.jump_speed = -12

        # Player status
        self.status = "idle"
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False


    def import_character_assets(self):
        """
        Import the character assets.

        Loads and stores the character animations from the specified folder.
        """

        character_path = "semestr2\\lista6\\graphics\\player\\"
        self.animations = {"idle":[], "run":[], "jump":[], "fall":[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)


    def get_input(self):
        """Get the player's input."""

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.movement_direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.movement_direction.x = -1
            self.facing_right = False
        else:
            self.movement_direction.x = 0
        
        if keys[pygame.K_SPACE]:
            self.jump()


    def get_status(self):
        """Determine the player's current status."""

        if self.movement_direction.y < 0:
            self.status = "jump"
        elif self.movement_direction.y > 1:
            self.status = "fall"
        else:
            if self.movement_direction.x != 0:
                self.status = "run"
            else:
                self.status = "idle"
    

    def apply_gravity(self):
        """Apply gravity to the player's movement."""

        self.movement_direction.y += self.gravity
        self.rect.y += self.movement_direction.y


    def jump(self):
        """Make the player jump."""

        if self.on_ground:
            self.movement_direction.y = self.jump_speed
            self.jump_sound.play()


    def animation(self):
        """Animate the player."""

        anim = self.animations[self.status]
        
        # Lopping over animation indexes
        self.frame_index += self.animation_speed
        if self.frame_index >= len(anim):
            self.frame_index = 0

        image = anim[int(self.frame_index)].convert_alpha()

        if self.facing_right:
            self.image = image
        else:
            self.image = pygame.transform.flip(image, True, False)

        # Setting player rect
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)


    def get_damaged(self):
        """Handle the player getting damaged."""

        if not self.invincible:
            self.health -= 1
            self.damage_sound.play()
            self.invincible = True
            self.hurt_time = pygame.time.get_ticks()

    
    def invincibility_timer(self):
        """Track the duration of invincibility after getting damaged."""

        if self.invincible:
            current_time = pygame.time.get_ticks()
            if current_time - self.hurt_time >= self.invincibility_duration:
                self.invincible = False

    
    def show_invincibility(self):
        """Toggle the player's visibility during invincibility."""

        value = sin(pygame.time.get_ticks())
        if self.invincible:
            if value > 0:
                self.image.set_alpha(0)
            else:
                self.image.set_alpha(255)
        else:
            self.image.set_alpha(255)


    def get_score(self):
        """
        Get the player's current score.

        Returns:
            int: The player's score.
        """
         
        return self.score


    def update(self):
        """Update the player."""

        self.get_input()
        self.get_status()
        self.animation()
        self.invincibility_timer()
        self.show_invincibility()
