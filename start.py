import pygame
import sys
from time import time
pygame.init()
from constants import *
from textClass import Text
from coinClass import Coin
from obstacleClass import Obstacle
from secondClass import Second
from characterClass import Character


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Fenêtre avec grille')

text_player_one = Text('Player 1 is the tag', SCREEN_WIDTH - 25 * cell_size,0, 255, 78, 200)
text_player_two = Text('Player 2 is the tag', SCREEN_WIDTH - 25 * cell_size, 0, 98, 78, 200)
coin0 = Coin(SCREEN_WIDTH - 5 * cell_size, SCREEN_HEIGHT - 7 * cell_size)
coin1 = Coin(SCREEN_WIDTH - 10 * cell_size, SCREEN_HEIGHT - 8 * cell_size)
coin2 = Coin(SCREEN_WIDTH - 20 * cell_size, SCREEN_HEIGHT - 3 * cell_size)
coin3 = Coin(SCREEN_WIDTH - 17 * cell_size, SCREEN_HEIGHT - 13 * cell_size)
coin4 = Coin(SCREEN_WIDTH - 38 * cell_size, SCREEN_HEIGHT - 27 * cell_size)
coin5 = Coin(SCREEN_WIDTH - 30 * cell_size, SCREEN_HEIGHT - 13 * cell_size)
obstacle = Obstacle(SCREEN_WIDTH - cell_size, SCREEN_HEIGHT- cell_size, 255, 0, 0, 1, 1)
obstacle2 = Obstacle(0, 0, 0, 0, 0, 1, 1)
obstacle3 = Obstacle(SCREEN_WIDTH - 3 * cell_size, SCREEN_HEIGHT - 3 * cell_size, 0, 255, 0, 2, 2)
obstacle4 = Obstacle(SCREEN_WIDTH - 30 * cell_size, SCREEN_HEIGHT - 20 * cell_size, 56, 45, 100, 10, 2)

all_sprites = pygame.sprite.Group()
coins = pygame.sprite.Group(coin0, coin1, coin2, coin3, coin4, coin5)
obstacles = pygame.sprite.Group(obstacle, obstacle2, obstacle3, obstacle4)
character = Character(SCREEN_WIDTH - cell_size, 0)
second_character = Second(SCREEN_WIDTH // 2 - cell_size // 2, SCREEN_HEIGHT // 2 - cell_size // 2)

all_sprites.add(character, second_character, coin0, coin1, coin2, coin3, coin4, coin5, obstacle, obstacle2, obstacle3, obstacle4)
coins.add(coin0, coin1, coin2, coin3, coin4, coin5)
obstacles.add(obstacle, obstacle2, obstacle3, obstacle4)

run = True
player_one_turn = True
print('Player one is the tag')
start = time()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    all_sprites.update(keys, obstacles)
    
    money_collisions = pygame.sprite.spritecollide(character, coins, True)
    money0_collisions = pygame.sprite.spritecollide(second_character, coins, True)
    for coin in money_collisions:
        print('Coin collected by player 1')
        character.points += 1

    for coin in money0_collisions:
        print('Coin collected by player 2')
        second_character.points += 1
    
    screen.fill((255, 255, 255))
    for x in range(0, SCREEN_WIDTH, cell_size):
        pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, cell_size):
        pygame.draw.line(screen, (0, 0, 0), (0, y), (SCREEN_WIDTH, y))
    
    all_sprites.draw(screen)
    obstacles.draw(screen)
    coins.draw(screen)

    collisions = pygame.sprite.spritecollide(character, all_sprites, False)
    current_time = time()
    if current_time - start >= 15 and player_one_turn:
        second_character.points += 15
        player_one_turn = False
        new_time = time()
        game_points = character.points
        game_points2 = second_character.points
        all_sprites = pygame.sprite.Group()
        coins = pygame.sprite.Group(coin0, coin1, coin2, coin3, coin4, coin5)
        obstacles = pygame.sprite.Group(obstacle, obstacle2, obstacle3, obstacle4)
        character = Character(SCREEN_WIDTH - cell_size, 0)
        second_character = Second(SCREEN_WIDTH // 2 - cell_size // 2, SCREEN_HEIGHT // 2 - cell_size // 2)
        all_sprites.add(character, second_character, coin0, coin1, coin2, coin3, coin4, coin5, obstacle, obstacle2, obstacle3, obstacle4)
        coins.add(coin0, coin1, coin2, coin3, coin4, coin5)
        obstacles.add(obstacle, obstacle2, obstacle3, obstacle4)
    if character in collisions and second_character in collisions and player_one_turn:
        time_touch = current_time - start
        print(f'{time_touch:.2f}')
        print("Collision detected! Player 1 touched player 2.")
        print('Player 2 is the tag')
        second_character.points += int(time_touch)
        player_one_turn = False
        game_points = character.points
        game_points2 = second_character.points
        all_sprites = pygame.sprite.Group()
        coins = pygame.sprite.Group(coin0, coin1, coin2, coin3, coin4, coin5)
        obstacles = pygame.sprite.Group(obstacle, obstacle2, obstacle3, obstacle4)
        character = Character(SCREEN_WIDTH - cell_size, 0)
        second_character = Second(SCREEN_WIDTH // 2 - cell_size // 2, SCREEN_HEIGHT // 2 - cell_size // 2)
        all_sprites.add(character, second_character, coin0, coin1, coin2, coin3, coin4, coin5, obstacle, obstacle2, obstacle3, obstacle4)
        coins.add(coin0, coin1, coin2, coin3, coin4, coin5)
        obstacles.add(obstacle, obstacle2, obstacle3, obstacle4)
        new_time = time()
    elif not player_one_turn:
        text_player_two.draw(screen)
        time_second = time()
        if time_second - new_time >= 15:
            print("Player 1 survived for 15 seconds! The game is over")
            character.points += game_points
            second_character.points += game_points2
            run = False
            character.points += 15
        elif character in collisions and second_character in collisions and not player_one_turn:
            time_second = time()
            time_touch_second = time_second - new_time
            print(f'{time_touch_second:.2f}')
            character.points += int(time_touch_second)
            print("Collision detected! Player 2 touched player 1.")
            print('The game is over')
            character.points += game_points
            second_character.points += game_points2
            run = False
    if player_one_turn:
        text_player_one.draw(screen)
    
    pygame.display.flip()
    pygame.display.update()

print(f'Player 1 has {character.points} points - Player 2 has {second_character.points} points')
pygame.quit()
sys.exit()
