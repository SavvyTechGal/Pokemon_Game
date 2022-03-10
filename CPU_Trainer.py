from Pokemon import Pokemon
import pokemon_db
import random
class CPU_Trainer:
    def __init__(self, name: str, gender: str, nature: str, fun_fact: str, img, special_pokemon = None):
        self.name = name
        self.gender = gender
        self.nature = nature
        self.fun_fact = fun_fact
        self.img = img
        self.number_of_pokemon = random.choice(range(1, 2))
        self.pokemon_list = []
        last_pokemon_type = None #used so that cpu trainer can only have pokemon of different types
        pokemon_type = None
        for i in range(self.number_of_pokemon):
            while last_pokemon_type == pokemon_type:
                pokemon_type = random.choice(pokemon_db.pokemon_array)
            self.pokemon_list.append(random.choice(pokemon_type))
            last_pokemon_type = pokemon_type
        self.pokemon_to_win = random.choice(self.pokemon_list)
        self.money_to_win = random.choice(range(20, 150))

        #used to specify that a cpu trainer has a certain pokemon to win
        if special_pokemon != None:
            self.special_pokemon = special_pokemon
            self.pokemon_list.append(self.special_pokemon)
            self.pokemon_to_win = self.special_pokemon

    def see_my_pokemon(self):
        print()
        print(f"{self.name}'s Pokemon")
        for pokemon in self.pokemon_list:
            print(f"Pokemon: {pokemon.name} Nature: {pokemon.nature}")
            print(pokemon.pokemon_display) 
        print()
    
    def print_trainer_details(self):
        details = f"Trainer: {self.name} Gender: {self.gender} Fun Fact: {self.fun_fact} Nature: "
        for row in self.nature:
            details+= f"{row}"
        return details

