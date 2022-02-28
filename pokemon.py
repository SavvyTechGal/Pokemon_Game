from ast import walk
import random
import climage
from colored import fg, bg, attr
import emoji

class Player:
    def __init__(self, name: str, gender: str, avatar, nature: str, pokemon_list: list, bag: list, money: int):
        self.name = name
        self.gender = gender
        self.avatar = avatar
        #(kind, mean, ect)
        self.nature = nature 
        self.pokemon_list = pokemon_list
        self.bag = bag
        self.money = money

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

class CPU_Trainer:
    def __init__(self, name: str, gender: str, nature: str, fun_fact: str, avatar, pokemon_list: list, pokemon_to_win: Pokemon, money_to_win: int):
        self.name = name
        self.gender = gender
        self.nature = nature
        self.fun_fact = fun_fact
        self.avatar = avatar 
        self.pokemon_list = pokemon_list
        self.pokemon_to_win = pokemon_to_win
        self.money_to_win = money_to_win

class Item:
    def __init__(self, name: str, img, capability: str):
        self.name = name #name of item
        self.img = img #img representation 
        self.capability = capability #description of what it does or allows you to do (ex: can allow other areas of the map to be walked on/entered)

class Terrain:
    def __init__(self, type: str, color, img, needs_item_to_move: bool, required_item: Item = None):
        self.type = type
        self.color = color
        self.img = img
        self.needs_item_to_move = needs_item_to_move #(ex: need flippers to swim, boots for mountains, heat-resistant cloak to go to the desert, cold-resistant cloak to go to ice/snow capped areas)
        if(self.needs_item_to_move):
            self.required_item = required_item
        else: 
            self.required_item = None

class Grid_Tile:
    def __init__(self, terrain: Terrain, is_object_on_tile: bool, object = None):
        self.terrain = terrain
        self.is_object_on_tile = is_object_on_tile
        if(is_object_on_tile):
            #accepted objects: pokemon aka wild pokemon, cpu_trainer, item 
            self.object = object

class Grid:
    def __init__(self):
        self.grid = [["-" for i in range(30)] for i in range(30)]
        #required map items
        #found in forest
        mountain_boots = Item("Mysterious Mountatin Boots", climage.convert('item_images/mysterious_mountain_boots3.png', is_unicode=True, width=3).rstrip(), "Allows you to enter the Volcanic Mountains!")
        
        #found in ice/snow area
        flippers = Item("Magic Flippers", climage.convert('item_images/magic_flippers.png', is_unicode=True, width=3).rstrip(), "Allows you to swim!")
        
        #test pokemon image
        # pokemon1 = Item("Pokemon", (' ' + "\u2744" + 'P'), "Allows you to swim!")
        
        #island in the middle of the lake
        desert_cloak = Item("Desert Cloak", climage.convert('item_images/desert_cloak.png', is_unicode=True, width=3).rstrip(), "Heat-Resistant Desert Cloak, Allows you to travel the desert at a comfortable temperature!")
        
        #found in mountains
        snow_coat = Item("Fluffy Snow Coat", climage.convert('item_images/fluffy_snow_coat.png', is_unicode=True, width=3).rstrip(), "Keeps you warm in snow and icy regions, No frost bite!")

        #required terrain tiles
        mountain_terrain = Terrain("Death Mountain", bg('#CF1020'), climage.convert('terrain_images/mountain.png', is_unicode=True, width=3).rstrip(), True, mountain_boots)
        grass_terrain = Terrain("grass", bg('#32a852'), climage.convert('terrain_images/grass.png', is_unicode=True, width=3).rstrip(), False)
        forest_terrain = Terrain("Viridian Forest", bg('#32a852'), climage.convert('terrain_images/tree.png', is_unicode=True, width=3).rstrip(), False)
        snow_terrain = Terrain("Snow Point Ruins", bg('#32a852'), climage.convert('terrain_images/snow.png', is_unicode=True, width=3).rstrip(), False)
        water_terrain = Terrain("Lake Hylia", bg('#32a852'), climage.convert('terrain_images/lake.png', is_unicode=True, width=3).rstrip(), False)
        desert_terrain = Terrain("Amon Desert Ruins", bg('#32a852'), climage.convert('terrain_images/sand.png', is_unicode=True, width=3).rstrip(), False)
        cherry_terrain = Terrain("Cherry Blossom Forest", bg('#32a852'), climage.convert('terrain_images/cherry.png', is_unicode=True, width=3).rstrip(), False)

        #mountain grid
        i_place = random.randint(0, 9)
        j_place = random.randint(0, 9)
        for i in range(10):
            for j in range(10):
                self.grid[i][j] = Grid_Tile(mountain_terrain, False)
                #place snow_coat on random square on death mountain
                if ((i == i_place) & (j == j_place)):
                    self.grid[i][j] = Grid_Tile(mountain_terrain, True, snow_coat)
        
        #home/start grid 
        for i in range(10):
            for j in range(10,20):
                self.grid[i][j] = Grid_Tile(grass_terrain, False)
        
        #forest grid
        i_place = random.randint(0, 9)
        j_place = random.randint(20, 29)
        for i in range(10):
            for j in range(20,30):
                self.grid[i][j] = Grid_Tile(forest_terrain, False)
                #place mountain_boots on random square in Viridian Forest
                if ((i == i_place) & (j == j_place)):
                    self.grid[i][j] = Grid_Tile(forest_terrain, True, mountain_boots)
        
        #town grid
        for i in range(10, 20):
            for j in range(10):
                self.grid[i][j] = Grid_Tile(grass_terrain, False)

        #water grid        
        for i in range(10, 30):
            for j in range(10,20):
                self.grid[i][j] = Grid_Tile(water_terrain, False)
        
        #island grid
        i_place = random.randint(18, 21)
        j_place = random.randint(13, 16)
        for i in range(18, 22):
            for j in range(13,17):
                self.grid[i][j] = Grid_Tile(grass_terrain, False)
                #place desert_cloak on random square on the island
                if ((i == i_place) & (j == j_place)):
                    self.grid[i][j] = Grid_Tile(grass_terrain, True, desert_cloak)

        #Snow Point Ruins
        i_place = random.randint(10, 19)
        j_place = random.randint(20, 29)
        for i in range(10, 20):
            for j in range(20,30):
                self.grid[i][j] = Grid_Tile(snow_terrain, False)
            #place flipper on random square in snow point ruins
                if ((i == i_place) & (j == j_place)):
                    self.grid[i][j] = Grid_Tile(snow_terrain, True, flippers)

        #Amon Desert Ruins
        for i in range(20, 30):
            for j in range(10):
                self.grid[i][j] = Grid_Tile(desert_terrain, False)

        #Cherry Blossom Forest
        for i in range(20, 30):
            for j in range(20,30):
                self.grid[i][j] = Grid_Tile(cherry_terrain, False)

    def print_grid(self):
        for row in self.grid:
            for col in row:
                if (col.is_object_on_tile):
                    print(col.object.img, end='')
                else: 
                    print(col.terrain.img, end='')
            print()
        # for i in range(10):
        #     for j in range(10):
        #         print(self.grid[i][j].terrain.color + self.grid[i][j].terrain.img, end='')




# converts the image to print in terminal
# inform of ANSI Escape codes
# output = climage.convert('pokemon_images/pokemon_wise_bear.png', is_unicode=True)
# mountain = climage.convert('terrain_images/mountain.png', is_unicode=True)
# # prints output on console.
# print(mountain)

# color = bg('#CF1020')
# print (color + " ")

myGrid = Grid()
myGrid.print_grid()
print(emoji.emojize(' :thumbs_up:'), "HI")

#Next Steps: 
# Start Menu: Select Player, Select First Pokemon 
# To win capture four pokemon of different types. (have earth: mountain, wind:forest, fire:desert, water:lake, special:cherry )
# Implement movement of Player if tries to move on to tile that cant walk on yet print msg ex: ("You are unable to climb Death Mountain! It has been said; however, that mystical climbing boots are hidden, somewhere in Viridian Forest.")