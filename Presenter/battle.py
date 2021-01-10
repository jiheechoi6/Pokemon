import pygame

class Battle:
    def __init__(self):
        self.font = pygame.font.SysFont('monospace', 25)
        self.hp1 = None
        self.hp2 = None
        self.left1 = None
        self.left2 = None
        self.name1 = None
        self.name2 = None

    def draw_battle(self, pic1: str, pic2: str, hp1: int, hp2: int, name1: str, name2: str):
        self.hp1 = hp1
        self.hp2 = hp2
        self.left1 = hp1
        self.left2 = hp2
        screen = pygame.display.get_surface()
        pygame.draw.rect(screen, (193, 204, 80), (0, 0, 900, 700))
        pygame.draw.ellipse(screen, (0, 255, 0), (600, 50, 300, 150))
        pygame.draw.ellipse(screen, (0, 255, 0), (0, 300, 300, 150))
        image1 = pygame.image.load(pic1)
        image2 = pygame.image.load(pic2)
        screen.blit(image1, (50, 250))
        screen.blit(image2, (625, -5))
        pygame.draw.rect(screen, (0, 0, 0), (400, 300, 400, 150))
        pygame.draw.rect(screen, (255, 250, 250), (410, 310, 380, 130))
        pygame.draw.rect(screen, (0, 0, 0), (100, 50, 400, 150))
        pygame.draw.rect(screen, (255, 250, 250), (110, 60, 380, 130))
        pygame.draw.rect(screen, (0, 0, 0), (0, 500, 900, 200))
        pygame.draw.rect(screen, (255, 250, 250), (10, 510, 880, 180))
        label = self.font.render('A wild pokemon has appeared!', 1, (0, 0, 0))
        screen.blit(label, (15, 515))
        label = self.font.render('Press (Enter) to continue.', 1, (0, 0, 0))
        screen.blit(label, (15, 650))
        label = self.font.render(str(hp1) + '/' + str(hp1), 1, (0, 0, 0))
        screen.blit(label, (415, 315))
        label = self.font.render(str(hp2) + '/' + str(hp2), 1, (0, 0, 0))
        screen.blit(label, (115, 65))
        self.name1 = name1
        self.name2 = name2
        label = self.font.render(self.name1, 1, (0, 0, 0))
        screen.blit(label, (600, 315))
        label = self.font.render(self.name2, 1, (0, 0, 0))
        screen.blit(label, (300, 65))
        pygame.draw.line(screen, (0, 0, 128), (420, 400), (780, 400), 10)
        pygame.draw.line(screen, (0, 0, 128), (120, 150), (480, 150), 10)
        pygame.display.update()

    def choose(self):
        print("hi")
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
        label = self.font.render('Press the 1,2 or 3 key to continue.', 1, (0, 0, 0))
        screen.blit(label, (15, 650))
        pygame.display.update()

    def attack(self, damage: int, is_successful: bool):
        screen = pygame.display.get_surface()
        pygame.draw.rect(screen, (0, 0, 0), (0, 500, 900, 200))
        pygame.draw.rect(screen, (255, 250, 250), (10, 510, 880, 180))
        if not is_successful:
            label = self.font.render('You have lost ' + str(damage) + 'hp.', 1, (0, 0, 0))
            pygame.draw.rect(screen, (0, 0, 0), (400, 300, 400, 150))
            pygame.draw.rect(screen, (255, 250, 250), (410, 310, 380, 130))
            self.left1 = self.left1 - damage
            lost = max(0, self.left1)
            label1 = self.font.render(str(lost) + '/' + str(self.hp1), 1, (0, 0, 0))
            screen.blit(label1, (415, 315))
        else:
            label = self.font.render('Your opponent has lost ' + str(damage) + 'hp.', 1, (0, 0, 0))
            pygame.draw.rect(screen, (0, 0, 0), (100, 50, 400, 150))
            pygame.draw.rect(screen, (255, 250, 250), (110, 60, 380, 130))
            self.left2 = self.left2 - damage
            lost = max(0, self.left2)
            label1 = self.font.render(str(lost) + '/' + str(self.hp2), 1, (0, 0, 0))
            screen.blit(label1, (115, 65))
        screen.blit(label, (15, 515))

        pygame.draw.line(screen, (255, 0, 0), (420, 400), (780, 400), 10)
        pygame.draw.line(screen, (255, 0, 0), (120, 150), (480, 150), 10)
        remain1 = 360 * (self.left1 / self.hp1)
        remain2 = 360 * (self.left2 / self.hp2)
        pygame.draw.line(screen, (0, 0, 128), (420, 400), (max(420, 420 + remain1), 400), 10)
        pygame.draw.line(screen, (0, 0, 128), (120, 150), (max(120, 120 + remain2), 150), 10)
        label = self.font.render('Press (Enter) to continue.', 1, (0, 0, 0))
        screen.blit(label, (15, 650))
        label = self.font.render(self.name1, 1, (0, 0, 0))
        screen.blit(label, (600, 315))
        label = self.font.render(self.name2, 1, (0, 0, 0))
        screen.blit(label, (300, 65))
        pygame.display.update()

    def faint(self, is_successful: bool):
        screen = pygame.display.get_surface()
        pygame.draw.rect(screen, (0, 0, 0), (0, 500, 900, 200))
        pygame.draw.rect(screen, (255, 250, 250), (10, 510, 880, 180))
        if not is_successful:
            label = self.font.render('You have fainted.', 1, (0, 0, 0))
        else:
            label = self.font.render('Your opponent has fainted.', 1, (0, 0, 0))
        screen.blit(label, (15, 515))
        label = self.font.render('Press (Enter) to continue.', 1, (0, 0, 0))
        screen.blit(label, (15, 650))
        pygame.display.update()



