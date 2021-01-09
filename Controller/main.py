import sys
import pygame

from Presenter.graphics import Graphics


graphics = Graphics()
graphics.draw_start_game_screen()

start_game_screen = True
grass_scene = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if start_game_screen:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 190 < event.pos[0] < 690 and 270<event.pos[1]<379:
                    graphics.draw_grass_scene()
                    grass_scene = True
                    start_game_screen = False
        if grass_scene:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    graphics.draw_moving_player(True, False, False, False)
                if event.key == pygame.K_DOWN:
                    graphics.draw_moving_player(False, False, True, False)
                if event.key == pygame.K_LEFT:
                    print("left")
                    graphics.draw_moving_player(False, False, False, True)
                if event.key == pygame.K_RIGHT:
                    graphics.draw_moving_player(False, True, False, False)
