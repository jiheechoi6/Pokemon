from Entity.pokemon import Pokemon

class PokemonBot(Pokemon):
    def __init__(self, pokemon_type: int):
        if pokemon_type == 0:
            max_hp = 60
            pic = '../img/pokemon_1_small.png'
            name = 'Togepi'
        elif pokemon_type == 1:
            max_hp = 70
            pic = '../img/pika.png'
            name = 'Pikachu'
        elif pokemon_type == 2:
            max_hp = 80
            pic = '../img/mimikyu.png'
            name = 'Mimikyu'
        elif pokemon_type == 3:
            max_hp = 90
            pic = '../img/lugia.png'
            name = 'Lugia'
        else:
            max_hp = 100
            pic = '../img/pokemon_2_small.png'
            name = 'Bulbasaur'
        super().__init__(pokemon_type, max_hp, pic, name)