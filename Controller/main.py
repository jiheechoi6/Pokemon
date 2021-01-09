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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_game_screen:
                if 190 < event.pos[0] < 690 and 270<event.pos[1]<379:
                    graphics.draw_grass_scene()
                    grass_scene = True
                    start_game_screen = False
