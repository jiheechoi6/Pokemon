class PokemonBot:
    _hp: int
    _max_hp: int
    _pokemon_type: int

    def __init__(self, pokemon_type: int):
        self._pokemonType = pokemon_type
        if pokemon_type == 0:
            self._max_hp = 60
        elif pokemon_type == 1:
            self._max_hp = 70
        elif pokemon_type == 2:
            self._max_hp = 80
        elif pokemon_type == 3:
            self._max_hp = 90
        else:
            self._max_hp = 100

    def updateHp(self, hp: int):
        self._hp += hp

    def getPokemonType(self):
        return self._pokemon_type

    def get_hp(self):
        return self._hp

    def get_max_hp(self):
        return self._max_hp
