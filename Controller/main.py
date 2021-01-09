import sys
import pygame

from Presenter.graphics import Graphics


graphics = Graphics()
graphics.draw_start_game_screen()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
