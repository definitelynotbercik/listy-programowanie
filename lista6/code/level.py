import pygame
from tiles import Tile
from barrier import Barrier
from coins import Coin
from settings import tile_size, coin_size, WIDTH
from player import Player
from enemy import Enemy
from explosion import Explosion
from goal import Goal


class Level():
    def __init__(self, level_data, surface):
        """
        Initialize the Level object.

        Args:
            level_data (list): The layout of the level.
            surface (pygame.Surface): The surface to display the level on.
        """
        
        self.display_surface = surface
        self.setup_level(level_data)

        self.world_move = 0
        
        self.x_collision = 0

        # Sound
        self.coin_sound = pygame.mixer.Sound("semestr2\lista6\sounds\coin_pickup.wav")
        self.enemy_death_sound = pygame.mixer.Sound("semestr2\lista6\sounds\enemy_death.wav")
        self.goal_sound = pygame.mixer.Sound("semestr2\\lista6\\sounds\\next_lvl.wav")

    
    def setup_level(self, layout):
        """
        Set up the level based on the given layout.

        Args:
            layout (list): The layout of the level.
        """

        # Groups
        self.tiles = pygame.sprite.Group()
        self.barriers = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.goal = pygame.sprite.GroupSingle()
        self.enemies = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.explosion_sprites = pygame.sprite.Group()

        # Creating map and player
        for row_index, row in enumerate(layout):
            for column_index, cell in enumerate(row):
                x = column_index * tile_size
                y = row_index * tile_size
                x_coin = x + 25
                y_coin = y + 25
                x_key = x + 20
                y_key = y + 20
                x_enemy = x
                y_enemy = y + 35
                if cell == "X":
                    tile = Tile((x,y), tile_size, "filler")
                    self.tiles.add(tile)
                if cell == "G":
                    tile = Tile((x,y), tile_size, "grass")
                    self.tiles.add(tile)
                if cell == "B":
                    tile = Barrier((x,y), tile_size)
                    self.barriers.add(tile)
                if cell == "C":
                    tile = Coin((x_coin, y_coin), coin_size)
                    self.coins.add(tile)
                if cell == "E":
                    tile = Enemy((x_enemy, y_enemy))
                    self.enemies.add(tile)
                if cell == "K":
                    tile = Goal((x_key,y_key), coin_size)
                    self.goal.add(tile)
                if cell == "P":
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
                    
    def move_camera(self):
        """Move the camera based on the player's position."""

        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.movement_direction.x

        if player_x < WIDTH/4 and direction_x < 0:
            self.world_move = 5
            player.speed = 0
        elif player_x > WIDTH-WIDTH/4 and direction_x > 0:
            self.world_move = -5
            player.speed = 0
        else:
            self.world_move = 0
            player.speed = 5
    
    def horizontal_collision(self):
        """Handle horizontal collisions between the player and tiles."""

        player = self.player.sprite

        player.rect.x += player.movement_direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.movement_direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.x_collision = player.rect.left
                elif player.movement_direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.x_collision = player.rect.right

        if player.on_left and (player.rect.left < self.x_collision or player.movement_direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.x_collision or player.movement_direction.x <= 0):
            player.on_right = False

    def vertical_collision(self):
        """Handle vertical collisions between the player and tiles."""

        player = self.player.sprite

        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.movement_direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.movement_direction.y = 0
                    player.on_ground = True
                elif player.movement_direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.movement_direction.y = 0
                    player.on_ceiling = True
        
        if player.on_ground and player.movement_direction.y < 0 or player.movement_direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.movement_direction.y > 0:
            player.on_ceiling = False


    def coin_collision(self):
        """Handle collisions between the player and coins."""

        player = self.player.sprite

        for sprite in self.coins.sprites():
            if sprite.rect.colliderect(player.rect):
                player.score += 3
                self.coin_sound.play()
                sprite.kill()

    
    def goal_collision(self):
        """Handle collisions between the player and goal."""

        player = self.player.sprite
        goal = self.goal.sprite

        if goal.rect.colliderect(player.rect):
            self.goal_sound.play()
            return True


    def enemy_collision(self):
        """Handle collisions between the player and enemies."""

        enemy_collisions = pygame.sprite.spritecollide(self.player.sprite, self.enemies, False)

        if enemy_collisions:
            for enemy in enemy_collisions:
                enemy_center = enemy.rect.centery
                enemy_top = enemy.rect.top
                player_bottom = self.player.sprite.rect.bottom
                if enemy_top < player_bottom < enemy_center and self.player.sprite.movement_direction.y >= 0:
                    self.player.sprite.movement_direction.y = self.player.sprite.jump_speed
                    explosion_sprite = Explosion(enemy.rect.center)
                    self.explosion_sprites.add(explosion_sprite)
                    enemy.kill()
                    self.enemy_death_sound.play()
                    self.player.sprite.score += 1
                else:
                    self.player.sprite.get_damaged()


    def get_player_score(self):
        """
        Get the player's current score.

        Returns:
            int: The player's score.
        """

        return self.player.sprite.score
    

    def get_player_health(self):
        """
        Get the player's current health.

        Returns:
            int: The player's health.
        """

        return self.player.sprite.health


    def check_fall(self):
        """Check if the player has fallen off the map."""

        if self.player.sprite.rect.y >= 800:
            self.player.sprite.health = 0


    def enemy_movement(self):
        """Handle enemy movement and collisions with barriers."""

        for enemy in self.enemies.sprites():
            for barrier in self.barriers.sprites():
                if enemy.rect.colliderect(barrier):
                    enemy.reverse()


    def generate(self):
        """Generate the level and update the game state."""

        # Tiles
        self.tiles.update(self.world_move)
        self.tiles.draw(self.display_surface)

        # Barriers
        self.barriers.update(self.world_move)
        self.barriers.draw(self.display_surface)

        # Coins
        self.coins.update(self.world_move)
        self.coins.draw(self.display_surface)

        # Goal
        self.goal.update(self.world_move)
        self.goal.draw(self.display_surface)

        # Enemies
        self.enemies.update(self.world_move)
        self.enemy_movement()
        self.enemies.draw(self.display_surface)

        # Explosion
        self.explosion_sprites.update(self.world_move)
        self.explosion_sprites.draw(self.display_surface)

        # Camera movement
        self.move_camera()

        # Player
        self.horizontal_collision()
        self.vertical_collision()
        self.coin_collision()
        self.player.update()
        self.player.draw(self.display_surface)
        self.enemy_collision()
        self.check_fall()
        