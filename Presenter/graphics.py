import pygame


class Graphics:
    def __init__(self):
        pygame.display.set_mode((900, 700))
        pygame.init()

    def draw_start_game_screen(self):
        screen = pygame.display.get_surface()
        pygame.draw.rect(screen, (255, 128, 128), (0, 0, 900, 700))
        image = pygame.image.load('./img/start_game_button.png')
        screen.blit(image, (190, 270))

        pygame.display.update()


    def draw_grass_scene(self):
        screen = pygame.display.get_surface()
        pygame.draw.rect(screen, (193, 204, 80), (0, 0, 900, 700)) # set background to green
        image = pygame.image.load('./img/grass.png')

        # draw grass (17 horizontally 6 vertically)
        for i in range(17):
            for j in range(6):
                screen.blit(image, (51*i+25, 40*j+460))

        pygame.display.update()

    
