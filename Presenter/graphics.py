import random
from typing import List, Tuple

import pygame


class Graphics:
    # grass scene attributes
    _door_positions: List[Tuple[int, int]]
    _player_pos: List[int]

    def __init__(self):
        self._door_positions = []
        pygame.display.set_mode((900, 700))
        pygame.init()

    def draw_start_game_screen(self):
        screen = pygame.display.get_surface()
        pygame.draw.rect(screen, (255, 128, 128), (0, 0, 900, 700))
        image = pygame.image.load('../img/start_game_button.png')
        screen.blit(image, (190, 270))

        pygame.display.update()

    def create_random_door_positions(self):
        for i in range(17):
            draw = random.randint(0, 6)  # random door position
            draw2 = random.randint(0, 6)  # random door position
            for j in range(8):
                x_pos = 51*i+25
                y_pos = 50*j+450
                if j == draw or j == draw2:
                    self._door_positions.append((x_pos, y_pos))

    def draw_grass_scene(self):
        screen = pygame.display.get_surface()
        pygame.draw.rect(screen, (193, 204, 80), (0, 0, 900, 700)) # set background to green
        image = pygame.image.load('../img/door.png')
        image2 = pygame.image.load('../img/grass2.png')

        # draw door and grass
        self.create_random_door_positions()
        for door_position in self._door_positions:
            screen.blit(image, (door_position[0], door_position[1]))
        for i in range(17):
            for j in range(8):
                x_pos = 51*i+24
                y_pos = 50*j+471
                screen.blit(image2, (x_pos, y_pos))

        # draw player
        player_img = pygame.image.load('../img/egg.png')
        screen.blit(player_img, (420, 300))
        self._player_pos = [420, 300]

        pygame.display.update()

    def draw_moving_player(self, up:bool, right:bool, down: bool, left: bool):
        screen = pygame.display.get_surface()
        player_img = pygame.image.load('../img/egg.png')
        image = pygame.image.load('../img/door.png')
        image2 = pygame.image.load('../img/grass2.png')

        if up:
            self._player_pos[1] -= 10
        elif right:
            self._player_pos[0] += 10
        elif down:
            self._player_pos[1] += 10
        else:
            self._player_pos[0] -= 10

        # draw door and grass
        pygame.draw.rect(screen, (193, 204, 80), (0, 0, 900, 700)) # set background to green
        for door_position in self._door_positions:
            screen.blit(image, (door_position[0], door_position[1]))
        for i in range(17):
            for j in range(8):
                x_pos = 51*i+24
                y_pos = 50*j+471
                screen.blit(image2, (x_pos, y_pos))

        screen.blit(player_img, (self._player_pos[0], self._player_pos[1]))
        pygame.display.update()


