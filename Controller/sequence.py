from Usecase.match import Match
from Usecase.game import Game
from Entity.player import Player

class sequence:
    def __init__(self):
        self.match = None
        self.pokemon_type = None

    def choose_pokemon(self, pokemon_type: int):
            self.pokemon_type = pokemon_type

    def start_match(self, p1: Player, p2: Player):
        self.match = Match(p1, p2)

    def round(self, move: int):
        botMove = Game.botAttack()
        if Game.matchingAttack(move, botMove):
            self.match.receive_attack(Game.get_damage_value(move))
        else:
            self.match.attack(Game.get_damage_value(move))


