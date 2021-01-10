import os, os.path
import sys
import pygame
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname("graphics.py"), '..')))
from Presenter.graphics import Graphics
from Presenter.battle import Battle
from Entity.pokemonBot import PokemonBot
from Entity.player import Player

graphics = Graphics()
battle = Battle()
graphics.draw_start_game_screen()

battle = Battle()

start_game_scene = True
choose_pokemon_scene = False
grass_scene = False
battle_scene = True
battle_result_scene = False # need to trigger this to true when game is over
player_type = -1 # making the player pokemon an int for easier backsprite handling
enemy_type = -1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if start_game_scene:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 190 < event.pos[0] < 690 and 270<event.pos[1]<379:
                    graphics.draw_choose_a_pokemon()
                    choose_pokemon_scene = True
                    start_game_scene = False
        elif choose_pokemon_scene:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 80 < event.pos[0] < 230 and 270 < event.pos[1] < 420:
                    player_type = 0
                if 370 < event.pos[0] < 520 and 270 < event.pos[1] < 420:
                    player_type = 1
                if 640 < event.pos[0] < 790 and 270 < event.pos[1] < 420:
                    player_type = 2
                player = Player(player_type)
                graphics.draw_grass_scene(player_type)
                grass_scene = True
                choose_pokemon_scene = False
        elif grass_scene:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    graphics.draw_moving_player(True, False, False, False)
                if event.key == pygame.K_DOWN:
                    graphics.draw_moving_player(False, False, True, False)
                if event.key == pygame.K_LEFT:
                    graphics.draw_moving_player(False, False, False, True)
                if event.key == pygame.K_RIGHT:
                    graphics.draw_moving_player(False, True, False, False)
                if event.key == pygame.K_RETURN: # TODO: check for if player overlaps with door
                    enemy_type = random.randint(0,5) # randomly generates a pkmn
                    grass_scene = False
                    battle_scene = True
        elif battle_scene:
            enemy = PokemonBot(enemy_type)
            battle.draw_battle(player.get_overworld_sprite(), enemy.get_pic(), player.get_hp(), enemy.get_hp(), player.get_name(), enemy.get_name())
        elif battle_result_scene:
            graphics.draw_battle_result(True) #hard coded to player win for now

