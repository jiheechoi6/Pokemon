import random

from Entity.player import Player
from Entity.pokemonBot import PokemonBot


# Every time a new match starts, a new instance of Match is created
class Match:
    _players: Player
    _pokemon_bot: PokemonBot
    _attacked: bool

    def __init__(self, pokemon_type: int):
        self._player = Player(pokemon_type)
        self._pokemon_bot = PokemonBot(random.randint(5))
        self._attacked = None

    def attack(self, attack_strength: int) -> None:
        self._pokemon_bot.updateHp(-attack_strength)
        self._attacked = True

    def receive_attack(self, attack_strength: int) -> None:
        self._player.updateHp(-attack_strength)
        self._attacked = False

    def is_game_over(self):
        if self._player.get_hp() <= 0:
            return True
        if self._pokemon_bot.get_hp() <= 0:
            return True
        return False
    
    def is_player_win(self):
        if self._player.get_hp() <= 0:
            return False
        else:
            return True

