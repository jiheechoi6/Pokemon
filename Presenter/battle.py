import pygame

class Battle:
    def __init__(self):
        self.font = pygame.font.SysFont('monospace', 25)

    def draw_battle(self, pic1: str, pic2: str, hp1: int, hp2: int, name1: str, name2: str):
        screen = pygame.display.get_surface()
        pygame.draw.rect(screen, (193, 204, 80), (0, 0, 900, 700))
        pygame.draw.ellipse(screen, (0, 255, 0), (600, 50, 300, 150))
        pygame.draw.ellipse(screen, (0, 255, 0), (0, 300, 300, 150))
        image1 = pygame.image.load(pic1)
        image2 = pygame.image.load(pic2)
        screen.blit(image1, (150, 375))
        screen.blit(image2, (750, 100))
        pygame.draw.rect(screen, (0, 0, 0), (400, 300, 400, 150))
        pygame.draw.rect(screen, (255, 250, 250), (410, 310, 380, 130))
        pygame.draw.rect(screen, (0, 0, 0), (100, 50, 400, 150))
        pygame.draw.rect(screen, (255, 250, 250), (110, 60, 380, 130))
        pygame.draw.rect(screen, (0, 0, 0), (0, 500, 900, 200))
        pygame.draw.rect(screen, (255, 250, 250), (10, 510, 880, 180))
        label = self.font.render('A wild pokemon has appeared!', 1, (0, 0, 0))
        screen.blit(label, (15, 515))
        label = self.font.render(str(hp1) + '/' + str(hp1), 1, (0, 0, 0))
        screen.blit(label, (415, 315))
        label = self.font.render(str(hp2) + '/' + str(hp2), 1, (0, 0, 0))
        screen.blit(label, (115, 65))
        label = self.font.render(name1, 1, (0, 0, 0))
        screen.blit(label, (600, 315))
        label = self.font.render(name2, 1, (0, 0, 0))
        screen.blit(label, (300, 65))
        pygame.display.update()

    def choose(self):
        screen = pygame.display.get_surface()
        pygame.draw.rect(screen, (0, 0, 0), (0, 500, 900, 200))
        pygame.draw.rect(screen, (255, 250, 250), (10, 510, 880, 180))
        label = self.font.render('Choose your next move:', 1, (0, 0, 0))
        screen.blit(label, (15, 515))
        label = self.font.render('(1) 5 hp', 1, (0, 0, 0))
        screen.blit(label, (15, 535))
        label = self.font.render('(2) 10 hp', 1, (0, 0, 0))
        screen.blit(label, (15, 555))
        label = self.font.render('(3) 15 hp', 1, (0, 0, 0))
        screen.blit(label, (15, 575))
        pygame.display.update()

    def attack(self, damage: int, is_successful: bool):
        screen = pygame.display.get_surface()
        pygame.draw.rect(screen, (0, 0, 0), (0, 500, 900, 200))
        pygame.draw.rect(screen, (255, 250, 250), (10, 510, 880, 180))
        if not is_successful:
            label = self.font.render('You have lost ' + damage + 'hp.', 1, (0, 0, 0))
            pygame.draw.rect(screen, (0, 0, 0), (400, 300, 400, 150))
            pygame.draw.rect(screen, (255, 250, 250), (410, 310, 380, 130))
            label1 = self.font.render(str(damage) + '/' + str(damage), 1, (0, 0, 0))
            screen.blit(label1, (415, 315))
        else:
            label = self.font.render('Your opponent has lost ' + damage + 'hp.', 1, (0, 0, 0))
            pygame.draw.rect(screen, (0, 0, 0), (100, 50, 400, 150))
            pygame.draw.rect(screen, (255, 250, 250), (110, 60, 380, 130))
            label1 = self.font.render(str(damage) + '/' + str(damage), 1, (0, 0, 0))
            screen.blit(label1, (115, 65))
        screen.blit(label, (115, 65))
        screen.blit(label, (15, 515))
        pygame.display.update()

    def faint(self, is_successful: bool):
        screen = pygame.display.get_surface()
        pygame.draw.rect(screen, (0, 0, 0), (0, 500, 900, 200))
        pygame.draw.rect(screen, (255, 250, 250), (10, 510, 880, 180))
        if is_successful:
            label = self.font.render('You have fainted.', 1, (0, 0, 0))
        else:
            label = self.font.render('Your opponent has fainted.', 1, (0, 0, 0))
        screen.blit(label, (15, 515))
        pygame.display.update()


