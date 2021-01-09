from Usecase.match import Match
from Usecase.game import Game

class sequence:
    def __init__(self):
        self.match = None
        self.pokemon_type = None

    def choose_pokemon(pokemon_type: int):
            self.pokemon_type = pokemon_type

    def start_match():
        if not self.pokemon_type:
            self.match = Match(self.pokemon_type)

    def round(self, move: int):
        botMove = Game.botAttack()
        if Game.matchingAttack(move, botMove):
            self.match.receive_attack(Game.get_damage_value(move))
        else:
            self.match.attack(Game.get_damage_value(move))


