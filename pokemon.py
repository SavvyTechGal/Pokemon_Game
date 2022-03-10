class Attack:
    def __init__(self, name: str, attack_type: str, strength: int):
        self.name = name
        #attack types (water, fire, wind, earth, martial_arts, special)
        self.attack_type = attack_type
        self.strength = strength

class Pokemon:
    def __init__(self, name: str, gender: str, type_of_pokemon: str, img, pokemon_display, nature: str, attacks: list, resistant_to_attack_of_type: str, health: int):
        self.name = name
        self.gender = gender
        self.type_of_pokemon = type_of_pokemon
        self.img = img
        self.pokemon_display = pokemon_display
        self.nature = nature
        #List of Attack objects
        self.attacks = attacks
        #Any attack type (ex: water, fire, wind, earth, martial_arts) pokemon is resistant to does half damage to pokemon
        self.resistant_to_attack_of_type = resistant_to_attack_of_type
        self.health = health