import sys
import pygame

from Presenter.graphics import Graphics


graphics = Graphics()
graphics.draw_start_game_screen()

start_game_scene = True
choose_pokemon_scene = False
grass_scene = False

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
                    graphics.draw_grass_scene(0)
                if 370 < event.pos[0] < 520 and 270 < event.pos[1] < 420:
                    graphics.draw_grass_scene(1)
                if 640 < event.pos[0] < 790 and 270 < event.pos[1] < 420:
                    graphics.draw_grass_scene(2)
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
