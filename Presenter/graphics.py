import pygame


class Graphics:
    def __init__(self):
        pygame.display.set_mode((900, 700))
        pygame.init()

    def draw_start_game_screen(self):
        screen = pygame.display.get_surface()
        image = pygame.image.load('start_game_button.png')
        pygame.transform.scale(image, (1, 1))
        screen.blit(image, (190, 270))

        pygame.display.update()
