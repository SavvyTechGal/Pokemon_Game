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
            print(f"{item.name} \n")
        print()

    def see_my_pokemon(self):
        print()
        print(f"{self.name}'s Pokemon")
        for pokemon in self.pokemon_list:
            print(f"Pokemon: {pokemon.name} Nature: {pokemon.nature} Health: {pokemon.health}")
            print(pokemon.pokemon_display) 
        print()
    
    def print_player_details(self):
        print(f"My Name: {self.name} Gender: {self.gender} Money: {self.money}")
        print("My Nature: ")
        for row in self.nature:
            print(f"{row}", end='')
        print()
