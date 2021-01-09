import pygame

class Battle:

    def draw_battle(self, pic1: str, pic2: str):
        screen = pygame.display.get_surface()
        pygame.draw.rect(screen, (193, 204, 80), (0, 0, 900, 700))
        oval1 = pygame.draw.ellipse(screen, (0, 255, 0), (600, 50, 300, 150))
        oval2 = pygame.draw.ellipse(screen, (0, 255, 0), (0, 300, 300, 150))
        image1 = pygame.image.load(pic1)
        image2 = pygame.image.load(pic2)
        screen.blit(image1, (150, 375))
        screen.blit(image2, (750, 100))
        rect = pygame.draw.rect(screen, (0, 0, 0), (400, 300, 400, 150))
        rect = pygame.draw.rect(screen, (255, 250, 250), (410, 310, 380, 130))
        rect = pygame.draw.rect(screen, (0, 0, 0), (100, 50, 400, 150))
        rect = pygame.draw.rect(screen, (255, 250, 250), (110, 60, 380, 130))
        rect = pygame.draw.rect(screen, (0, 0, 0), (0, 500, 900, 200))
        rect = pygame.draw.rect(screen, (255, 250, 250), (10, 510, 880, 180))
        font = pygame.font.SysFont('monospace', 25)
        label = font.render('A wild pokemon has appeared!', 1, (0, 0, 0))
        screen.blit(label, (15, 515))
        pygame.display.update()


