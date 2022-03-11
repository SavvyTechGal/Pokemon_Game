#Savana Hughes 23798928
#March 10th, 2022
#Advanced Python Pokemon Game
class Attack:
    def __init__(self, name: str, attack_type: str, strength: int):
        self.name = name
        #attack types 
        # 1. (element (water, fire, wind, earth) 
        # 2. martial_arts(puch, kick), 
        # 3. special (ice, lightening, tornado, metor_shower), 
        # 4. heal/defend)
        self.attack_type = attack_type
        self.strength = strength

class Pokemon:
    def __init__(self, name: str, gender: str, nature: str, attacks: list, resistant_to_attack_of_type: str, weak_to_attack_of_type: str, health: int, img, pokemon_display):
        self.name = name
        self.gender = gender
        self.img = img
        self.pokemon_display = pokemon_display
        self.nature = nature
        #List of Attack objects
        self.attacks = attacks
        #Any attack type (ex: water, fire, wind, earth, martial_arts) pokemon is resistant to does half damage to pokemon
        self.resistant_to_attack_of_type = resistant_to_attack_of_type
        self.weak_to_attack_of_type = weak_to_attack_of_type
        self.health = health
        self.start_health = health