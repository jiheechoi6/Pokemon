from Entity.pokemonBot import PokemonBot

class Player:
    _pokemon: PokemonBot

    def __init__(self, pokemon_type: int):
        self._pokemon = PokemonBot(pokemon_type)

    def updateHp(self, hp: int):
        self._hp += hp

    def get_hp(self):
        return self._hp
