import random
import string
from typing import List, Tuple

import pygame


class Graphics:
    # grass scene attributes
    _door_positions: List[Tuple[int, int]]
    _player_pos: List[int]
    _player_img_small: string

    def __init__(self):
        self._door_positions = []
        pygame.display.set_mode((900, 700))
        pygame.init()

    def draw_start_game_screen(self):
        screen = pygame.display.get_surface()
        background_img = pygame.image.load('../img/background.png')
        screen.blit(background_img, (0, 0))
        pygame.draw.rect(screen, (255, 228, 228), (167, 266, 540, 120))
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

    '''@param pokemon_type: the type of pokemon the player chose.
                            0 - the leftmost pokemon
                            1 - middle pokemon
                            2 - rightmost pokemon'''
    def draw_grass_scene(self, pokemon_type: int):
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

        if pokemon_type == 0:
            self._player_img_small = '../img/pokemon_0_small.png'
        elif pokemon_type == 1:
            self._player_img_small = '../img/pokemon_1_small.png'
        else:
            self._player_img_small = '../img/pokemon_2_small.png'

        player_img = pygame.image.load(self._player_img_small)

        screen.blit(player_img, (420, 300))
        self._player_pos = [420, 300]

        pygame.display.update()

    def draw_moving_player(self, up:bool, right:bool, down: bool, left: bool):
        screen = pygame.display.get_surface()
        player_img = pygame.image.load(self._player_img_small)
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

    def draw_choose_a_pokemon(self):
        print("check")
        screen = pygame.display.get_surface()
        background_img = pygame.image.load('../img/background_light.png')
        pokemon0_img = pygame.image.load('../img/pokemon_0.png')
        pokemon1_img = pygame.image.load('../img/pokemon_1.png')
        pokemon2_img = pygame.image.load('../img/pokemon_2.png')

        my_font = pygame.font.SysFont('freesansbold', 55)
        label = my_font.render("Choose a pokemon!", True, (0, 0, 0))

        screen.blit(background_img, (0, 0))
        screen.blit(label, (250, 150))  # instruction ("choose a pokemon")
        screen.blit(pokemon0_img, (80, 272))  # first pokemon
        screen.blit(pokemon1_img, (370, 280))  # second pokemon
        screen.blit(pokemon2_img, (640, 260))  # third pokemon

        pygame.display.update()
