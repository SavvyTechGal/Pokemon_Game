import functions
from Item import Item
from CPU_Trainer import CPU_Trainer
import pokemon_db
import inquirer
from inquirer.themes import GreenPassion
import random
import climage
from colored import fg, bg, attr #to make text/bg a specifc color 

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
    def __init__(self, terrain: Terrain, is_object_on_tile: bool, object = None, is_player_on_tile: bool = False, player = None, is_trainer_on_tile: bool = False, trainer = None):
        self.terrain = terrain
        self.is_object_on_tile = is_object_on_tile
        if(is_object_on_tile):
            #accepted objects: pokemon aka wild pokemon, cpu_trainer, item 
            self.object = object

        self.is_player_on_tile = is_player_on_tile
        if(is_player_on_tile):
            self.player = player
        
        self.is_trainer_on_tile = is_trainer_on_tile
        if(is_trainer_on_tile):
            self.trainer = trainer

class Grid:
    def __init__(self):
        self.grid = [["-" for i in range(30)] for i in range(30)]
        
        #init player
        self.my_player = functions.new_game_setup()
         
        #init required map items
        #found in forest
        mountain_boots = Item("Mysterious Mountatin Boots", climage.convert('item_images/mysterious_mountain_boots3.png', is_unicode=True, width=3).rstrip(), "Allows you to enter the Volcanic Mountains!")
        
        #found in mountains
        snow_coat = Item("Fluffy Snow Coat", climage.convert('item_images/fluffy_snow_coat.png', is_unicode=True, width=3).rstrip(), "Keeps you warm in snow and icy regions, No frost bite!")

        #found in ice/snow area
        flippers = Item("Magic Flippers", climage.convert('item_images/magic_flippers.png', is_unicode=True, width=3).rstrip(), "Allows you to swim!")
        
        #island in the middle of the lake
        desert_cloak = Item("Desert Cloak", climage.convert('item_images/desert_cloak.png', is_unicode=True, width=3).rstrip(), "Heat-Resistant Desert Cloak, Allows you to travel the desert at a comfortable temperature!")
        
        #hearts -> heals a fallen pokemon to full health
        heart = Item("Heart", ' \u2764\ufe0f ', 'Heals a fallen pokemon to full health. Can be used in battle or from bag in world.')
        

        #required terrain tiles
        grass_terrain = Terrain("grass", bg('#32a852'), climage.convert('terrain_images/grass.png', is_unicode=True, width=3).rstrip(), False)
        forest_terrain = Terrain("Viridian Forest", bg('#32a852'), climage.convert('terrain_images/tree.png', is_unicode=True, width=3).rstrip(), False)
        mountain_terrain = Terrain("Death Mountain", bg('#CF1020'), climage.convert('terrain_images/mountain.png', is_unicode=True, width=3).rstrip(), True, mountain_boots)
        snow_terrain = Terrain("Snow Point Ruins", bg('#32a852'), climage.convert('terrain_images/snow.png', is_unicode=True, width=3).rstrip(), True, snow_coat)
        water_terrain = Terrain("Lake Hylia", bg('#32a852'), climage.convert('terrain_images/lake.png', is_unicode=True, width=3).rstrip(), True, flippers)
        desert_terrain = Terrain("Amon Desert Ruins", bg('#32a852'), climage.convert('terrain_images/sand.png', is_unicode=True, width=3).rstrip(), True, desert_cloak)
        cherry_terrain = Terrain("Cherry Blossom Forest", bg('#32a852'), climage.convert('terrain_images/cherry.png', is_unicode=True, width=3).rstrip(), False)

        #home/start grid 
        for i in range(10):
            for j in range(10,20):
                self.grid[i][j] = Grid_Tile(grass_terrain, False)
                #place player at start
                if ((i == 1) & (j == 14)):
                    self.grid[i][j].is_player_on_tile = True 
                    self.grid[i][j].player = self.my_player 
                    self.my_player.location_x = j
                    self.my_player.location_y = i


        #forest grid
        i_place = random.randint(0, 9)
        j_place = random.randint(20, 29)
        for i in range(10):
            for j in range(20,30):
                self.grid[i][j] = Grid_Tile(forest_terrain, False)
                #place mountain_boots on random square in Viridian Forest
                if ((i == i_place) & (j == j_place)):
                    self.grid[i][j] = Grid_Tile(forest_terrain, True, mountain_boots)

        #place forest trainer -> win wind pokemon 
        i_cpu, j_cpu = functions.initialize_cpu_trainers(0, 8, 20, 28, self.grid)
        self.grid[i_cpu][j_cpu].is_trainer_on_tile = True
        self.grid[i_cpu][j_cpu].trainer = CPU_Trainer('Fern', 'Male', 'Kind, Still', 'One with the forest!', '\T/', random.choice(pokemon_db.wind_list))
        self.grid[i_cpu][j_cpu].trainer.see_my_pokemon()
        self.grid[i_cpu][j_cpu].trainer.print_trainer_details()
        #mountain grid
        i_place = random.randint(0, 9)
        j_place = random.randint(0, 9)
        for i in range(10):
            for j in range(10):
                self.grid[i][j] = Grid_Tile(mountain_terrain, False)
                #place snow_coat on random square on death mountain
                if ((i == i_place) & (j == j_place)):
                    self.grid[i][j] = Grid_Tile(mountain_terrain, True, snow_coat)

        #place mountain trainer -> win mountain pokemon 
        i_cpu, j_cpu = functions.initialize_cpu_trainers(0, 9, 0, 9, self.grid)
        self.grid[i_cpu][j_cpu].is_trainer_on_tile = True
        self.grid[i_cpu][j_cpu].trainer = CPU_Trainer('Ruth', 'Female', 'Brave, Tough', 'Can move Mountains if I try!', '\T/', random.choice(pokemon_db.earth_list))
        self.grid[i_cpu][j_cpu].trainer.see_my_pokemon()
        self.grid[i_cpu][j_cpu].trainer.print_trainer_details()
        
        #town grid
        for i in range(10, 20):
            for j in range(10):
                self.grid[i][j] = Grid_Tile(grass_terrain, False)
        #place  a fewrandom common trainer -> win a starter pokemon
        i_cpu, j_cpu = functions.initialize_cpu_trainers(10, 19, 0, 9, self.grid)
        self.grid[i_cpu][j_cpu].is_trainer_on_tile = True
        self.grid[i_cpu][j_cpu].trainer = CPU_Trainer('Tina', 'Female', 'Plain, Simple', 'Just hangin around', '\T/', random.choice(pokemon_db.starter_list))
        self.grid[i_cpu][j_cpu].trainer.see_my_pokemon()
        self.grid[i_cpu][j_cpu].trainer.print_trainer_details()

        i_cpu, j_cpu = functions.initialize_cpu_trainers(10, 19, 0, 9, self.grid)
        self.grid[i_cpu][j_cpu].is_trainer_on_tile = True
        self.grid[i_cpu][j_cpu].trainer = CPU_Trainer('Glind', 'Male', 'Bro, Figher', 'I lift weights all day long!', '\T/', random.choice(pokemon_db.starter_list))
        self.grid[i_cpu][j_cpu].trainer.see_my_pokemon()
        self.grid[i_cpu][j_cpu].trainer.print_trainer_details()
        
        #Snow Point Ruins
        i_place = random.randint(10, 19)
        j_place = random.randint(20, 29)
        for i in range(10, 20):
            for j in range(20,30):
                self.grid[i][j] = Grid_Tile(snow_terrain, False)
            #place flipper on random square in snow point ruins
                if ((i == i_place) & (j == j_place)):
                    self.grid[i][j] = Grid_Tile(snow_terrain, True, flippers)
        
        #place  a few random trainers -> could be super specialized!
        i_cpu, j_cpu = functions.initialize_cpu_trainers(10, 18, 20, 28, self.grid)
        self.grid[i_cpu][j_cpu].is_trainer_on_tile = True
        self.grid[i_cpu][j_cpu].trainer = CPU_Trainer('Lorea', 'Female', 'I love dancing!', '', '\T/')
        self.grid[i_cpu][j_cpu].trainer.see_my_pokemon()
        self.grid[i_cpu][j_cpu].trainer.print_trainer_details()

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
        
        #place  a fewrandom common trainer -> win a water pokemon
        i_cpu, j_cpu = functions.initialize_cpu_trainers(10, 28, 10, 18, self.grid)
        self.grid[i_cpu][j_cpu].is_trainer_on_tile = True
        self.grid[i_cpu][j_cpu].trainer = CPU_Trainer('Lilly', 'Female', 'Kind, Quiet, Brave', 'Super fast swimmer', '\T/', random.choice(pokemon_db.water_list))
        self.grid[i_cpu][j_cpu].trainer.see_my_pokemon()
        self.grid[i_cpu][j_cpu].trainer.print_trainer_details()

        #place  a fewrandom common trainer -> win a water pokemon
        i_cpu, j_cpu = functions.initialize_cpu_trainers(10, 28, 10, 18, self.grid)
        self.grid[i_cpu][j_cpu].is_trainer_on_tile = True
        self.grid[i_cpu][j_cpu].trainer = CPU_Trainer('Philip', 'Male', 'Princely, Dashing', 'I once kissed a sleeping princess and she woke up laughing...', '\T/', random.choice(pokemon_db.water_list))
        self.grid[i_cpu][j_cpu].trainer.see_my_pokemon()
        self.grid[i_cpu][j_cpu].trainer.print_trainer_details()

        #Amon Desert Ruins
        for i in range(20, 30):
            for j in range(10):
                self.grid[i][j] = Grid_Tile(desert_terrain, False)
        
        #place  a fewrandom common trainer -> win a fire pokemon
        i_cpu, j_cpu = functions.initialize_cpu_trainers(20, 29, 0, 9, self.grid)
        self.grid[i_cpu][j_cpu].is_trainer_on_tile = True
        self.grid[i_cpu][j_cpu].trainer = CPU_Trainer('Henry', 'Male', 'Cloud9', 'I am not sure where I am.', '\T/', random.choice(pokemon_db.fire_list))
        self.grid[i_cpu][j_cpu].trainer.see_my_pokemon()
        self.grid[i_cpu][j_cpu].trainer.print_trainer_details()
        i_cpu, j_cpu = functions.initialize_cpu_trainers(20, 29, 0, 9, self.grid)
        self.grid[i_cpu][j_cpu].is_trainer_on_tile = True
        self.grid[i_cpu][j_cpu].trainer = CPU_Trainer('Faith', 'Female', 'Magic, Firey, Blazy', 'Haha, no way you can beat me', '\T/', random.choice(pokemon_db.fire_list))
        self.grid[i_cpu][j_cpu].trainer.see_my_pokemon()
        self.grid[i_cpu][j_cpu].trainer.print_trainer_details()

        #Cherry Blossom Forest
        for i in range(20, 30):
            for j in range(20,30):
                self.grid[i][j] = Grid_Tile(cherry_terrain, False)
        
        #place  a few random trainers -> could be super specialized!
        i_cpu, j_cpu = functions.initialize_cpu_trainers(20, 29, 20, 29, self.grid)
        self.grid[i_cpu][j_cpu].is_trainer_on_tile = True
        self.grid[i_cpu][j_cpu].trainer = CPU_Trainer('Fiddle', 'Female', 'Lets catch em all!', '', '\T/')
        self.grid[i_cpu][j_cpu].trainer.see_my_pokemon()
        self.grid[i_cpu][j_cpu].trainer.print_trainer_details()
        
        i_cpu, j_cpu = functions.initialize_cpu_trainers(20, 29, 20, 29, self.grid)
        self.grid[i_cpu][j_cpu].is_trainer_on_tile = True
        self.grid[i_cpu][j_cpu].trainer = CPU_Trainer('Sid', 'Male', 'Got caught with my hand in a cookie jar...', '', '\T/')
        self.grid[i_cpu][j_cpu].trainer.see_my_pokemon()
        self.grid[i_cpu][j_cpu].trainer.print_trainer_details()

        #place 6 hearts randomly throughout the map
        for i in range(6):
            i_cpu, j_cpu = functions.initialize_cpu_trainers(1, 29, 1, 29, self.grid)
            self.grid[i_cpu][j_cpu].is_object_on_tile = True
            self.grid[i_cpu][j_cpu].object = heart


    def print_grid(self):
        for row in self.grid:
            for col in row:
                if (col.is_player_on_tile):
                    print(col.player.img, end='')
                elif (col.is_trainer_on_tile):
                    print(col.trainer.img, end='')
                elif (col.is_object_on_tile):
                    print(col.object.img, end='')
                else: 
                    print(col.terrain.img, end='')
            print()
    
    def place_player(self, x, y):
        self.grid[y][x].is_player_on_tile = True 
        self.grid[y][x].player = self.my_player 
    
    def remove_player(self, x, y):
        self.grid[y][x].is_player_on_tile = False
        self.grid[y][x].player = None
    
    def place_object(self, object, x, y):
        self.grid[y][x].is_object_on_tile = True 
        self.grid[y][x].object = object 
    
    def remove_object(self, x, y):
        self.grid[y][x].is_object_on_tile = False
        self.grid[y][x].object = None
    
    def input(self):
        while True:
            questions = [
                inquirer.Text("cmd", message="Use Keyboard to Control your Player - Type c to see list of commands")
            ]
            answers = inquirer.prompt(questions, theme=GreenPassion())

            #see list of commands 
            if answers['cmd'] == 'c':
                print('c: List of Commands \n w: move up \n a: move right \n s: move down \n d: move left \n space: interact with tile \n m: menu \n' 'q: quit game \n')
            
            #open menu
            if answers['cmd'] == 'm':
                run = True
                while run:
                    q = [
                        inquirer.List("menu_choice", message="MENU", choices=["My Bag", "My Pokemon", "Exit Menu"], default="My Bag"),
                    ]
                    menu_answer = inquirer.prompt(q, theme=GreenPassion()) 
                    if menu_answer['menu_choice'] == 'My Bag':
                        self.my_player.open_bag()
                    if menu_answer['menu_choice'] == 'My Pokemon':
                        self.my_player.see_my_pokemon()
                    if menu_answer['menu_choice'] == 'Exit Menu':
                        run = False
            
            #interact with tile
            if answers['cmd'] == ' ':
                tile = self.grid[self.my_player.location_y][self.my_player.location_x]
                if tile.is_object_on_tile:
                    if isinstance(tile.object, Item):
                        print(f"You have picked up {tile.object.name}.\n Capability {tile.object.capability}\n The item has been added to your bag!\n")
                        self.my_player.bag.append(tile.object)
                        self.remove_object(self.my_player.location_x, self.my_player.location_y)
                if tile.is_trainer_on_tile:
                    if isinstance(tile.trainer, CPU_Trainer):
                        print(f"Time to Battle!! You are Battling {tile.trainer.print_trainer_details()}.\n At the end of the battle you will win ${tile.trainer.money_to_win} and this Pokemon: \n {tile.trainer.pokemon_to_win.pokemon_display} Pokemon: {tile.trainer.pokemon_to_win.name} Nature: {tile.trainer.pokemon_to_win.nature}\n")
                        functions.battle(self.my_player, tile.trainer)
                        self.print_grid()
            #move up
            if answers['cmd'] == 'w':
                self.remove_player(self.my_player.location_x, self.my_player.location_y)
                self.my_player.location_y -= 1
                self.place_player(self.my_player.location_x, self.my_player.location_y)
                self.print_grid()

            #move left    
            if answers['cmd'] == 'a':
                self.remove_player(self.my_player.location_x, self.my_player.location_y)
                self.my_player.location_x -= 1
                self.place_player(self.my_player.location_x, self.my_player.location_y)
                self.print_grid()

            #move down
            if answers['cmd'] == 's':
                self.remove_player(self.my_player.location_x, self.my_player.location_y)
                self.my_player.location_y += 1
                self.place_player(self.my_player.location_x, self.my_player.location_y)
                self.print_grid()

            #move right
            if answers['cmd'] == 'd':
                self.remove_player(self.my_player.location_x, self.my_player.location_y)
                self.my_player.location_x += 1
                self.place_player(self.my_player.location_x, self.my_player.location_y)
                self.print_grid()
            
            #quit game
            if answers['cmd'] == 'q':
                quit_questions = [
                        inquirer.List("quit", message="Are you sure you want to quit the game? You will loose your progress!", choices=["Yes", "No"], default="No"),
                    ]
                quit = inquirer.prompt(quit_questions, theme=GreenPassion()) 
                if quit['quit'] == 'Yes':
                    print('Good Game!! See you soon!')
                    break



