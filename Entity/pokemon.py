''' The general Pokemon class.
Both the player and the enemy are subclasses of this.
'''

class Pokemon:
    _hp: int
    _max_hp: int
    _pokemon_type: int
    _pic: str
    _name: str

    def __init__(self, pokemon_type: int, max_hp: int, pic: str, name: str):
        self._pokemon_type = pokemon_type
        self._max_hp = max_hp
        self._hp = max_hp
        self._pic = pic
        self._name = name

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
