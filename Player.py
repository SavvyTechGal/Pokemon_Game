from Item import Item
from Pokemon import Pokemon
class Player:
    def __init__(self, name: str, gender: str, img, nature: list, pokemon_list: list, bag: list, money: int, location_x: int = None, location_y: int = None):
        self.name = name
        self.gender = gender
        self.img = img
        #(kind, mean, ect)
        self.nature = nature 
        self.pokemon_list = pokemon_list
        self.bag = bag
        self.money = money
        self.location_x = location_x
        self.location_y = location_y
    
    def open_bag(self):
        print()
        print("My Bag")
        for item in self.bag:
            print(item.name, end='')
        print()

    # def see_my_pokemon(self):
    #     print()
    #     print("My Pokemon")
    #     for pokemon in self.pokemon_list:
    #         print(pokemon, end='')
    #     print()

    def see_my_pokemon(self):
        print()
        print("My Pokemon")
        for pokemon in self.pokemon_list:
            print(pokemon.pokemon_display)
            print("Name: ", pokemon.name, " Nature: ", pokemon.nature)
        print()
    
    def print_nature(self):
        print()
        print("My Nature")
        for row in self.nature:
            print(row, end=' ')
        print()