class PokemonBot:
    _hp: int
    _max_hp: int
    _pokemon_type: int
    _pic: str

    def __init__(self, pokemon_type: int):
        self._pokemonType = pokemon_type
        if pokemon_type == 0:
            self._max_hp = 60
            self._pic = '../img/egg.png'
            self._name = 'name1'
        elif pokemon_type == 1:
            self._max_hp = 70
            self._pic = '../img/pika.png'
            self._name = 'name2'
        elif pokemon_type == 2:
            self._max_hp = 80
            self._pic = '../img/mimikyu.png'
            self._name = 'name3'
        elif pokemon_type == 3:
            self._max_hp = 90
            self._pic = '../img/lugia.png'
            self._pic = 'name4'
        else:
            self._max_hp = 100
            self._pic = '../img/egg.png'
            self._pic = 'name5'

    def updateHp(self, hp: int):
        self._hp += hp

    def getPokemonType(self):
        return self._pokemon_type

    def get_hp(self):
        return self._hp

    def get_max_hp(self):
        return self._max_hp

    def get_pic(self):
        return self._pic

    def get_name(self):
        return self._name
