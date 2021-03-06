from Usecase.match import Match
from Usecase.game import Game
from Entity.player import Player

class Sequence:
    def __init__(self):
        self.match = None
        self.pokemon_type = None
        self.game = Game()

    def choose_pokemon(self, pokemon_type: int):
            self.pokemon_type = pokemon_type

    def start_match(self, p1: Player, p2: Player):
        self.match = Match(p1, p2)

    def round(self, move: int):
        botMove = self.game.botAttack()
        if self.game.matchingAttack(move, botMove):
            self.match.receive_attack(self.game.get_damage_value(move))
            return False, self.game.get_damage_value(move)
        else:
            self.match.attack(self.game.get_damage_value(move))
            return True, self.game.get_damage_value(move)


