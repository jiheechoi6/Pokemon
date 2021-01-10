from Entity.pokemon import Pokemon

class Player(Pokemon):
    def __init__(self, pokemon_type: int):
        global pic
        global name
        # Dependent of what Pokemon the player chose in the beginning menu
        if pokemon_type == 0:
            pic = '../img/pokemon_0.png'
            name = 'Eevee'
        elif pokemon_type == 1:
            pic = '../img/pokemon_1.png'
            name = 'Togepi'
        elif pokemon_type == 2:
            pic = '../img/pokemon_2.png'
            name = 'Bulbasaur'
        super().__init__(pokemon_type, 80, pic, name)

    def __str__(self): # for debugging
        return f'{self.get_name()} - type: {self.getPokemonType()}'

    def get_overworld_sprite(self):
        return f'../img/pokemon_{self.getPokemonType()}_small.png'
    