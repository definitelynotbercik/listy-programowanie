import pygame
from tiles import Tile
from coins import Coin
from settings import tile_size, coin_size, WIDTH
from player import Player
from enemy import Enemy


class Level():
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)

        self.world_move = 0
        
        self.x_collision = 0

    
    def setup_level(self, layout):
        #Groups
        self.tiles = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.enemy = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        #Creating map and player
        for row_index, row in enumerate(layout):
            for column_index, cell in enumerate(row):
                x = column_index * tile_size
                y = row_index * tile_size
                x_coin = x + 25
                y_coin = y + 25
                x_enemy = x
                y_enemy = y + 35
                if cell == "X":
                    tile = Tile((x,y), tile_size, "filler")
                    self.tiles.add(tile)
                if cell == "G":
                    tile = Tile((x,y), tile_size, "grass")
                    self.tiles.add(tile)
                if cell == "C":
                    tile = Coin((x_coin, y_coin), coin_size)
                    self.coins.add(tile)
                if cell == "E":
                    tile = Enemy((x_enemy, y_enemy))
                    self.enemy.add(tile)
                if cell == "P":
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
                    
    def move_camera(self):
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
        player = self.player.sprite

        for sprite in self.coins.sprites():
            if sprite.rect.colliderect(player.rect):
                player.score += 1
                sprite.kill()


    def get_player_score(self):
        return self.player.sprite.score


    def generate(self):
        #Level
        self.tiles.update(self.world_move)
        self.tiles.draw(self.display_surface)
        self.coins.update(self.world_move)
        self.coins.draw(self.display_surface)
        self.enemy.update(self.world_move)
        self.enemy.draw(self.display_surface)
        self.move_camera()

        #Player
        self.horizontal_collision()
        self.vertical_collision()
        self.coin_collision()
        self.player.update()
        self.player.draw(self.display_surface)