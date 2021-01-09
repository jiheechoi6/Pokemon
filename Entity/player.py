class Player:
    _hp: int

    def __init__(self, hp: int):
        self._hp = hp

    def updateHp(self, hp: int):
        self._hp += hp

    def get_hp(self):
        return self._hp
