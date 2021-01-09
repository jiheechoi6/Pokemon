from Entity.player import Player
from Entity.pokemonBot import PokemonBot
from random import randint

class Game:
    def matchingAttack(p1: int, p2: int):
        return p1 == p2

    def botAttack():
        attack = randint(1, 6)
        if attack >= 4:
            return 3
        if attack >= 2:
            return 2
        return 1

    def get_damage_value(num: str):
        if num == 1:
            return 5
        if num == 2:
            return 10
        if num == 3:
            return 15