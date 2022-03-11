from tracemalloc import start
from turtle import st
from CPU_Trainer import CPU_Trainer
import inquirer
from inquirer.themes import GreenPassion
from Player import Player
import pokemon_db
import random
import copy


def new_game_setup():
    print('Pokemon Adventure: Alternate reality Zelda meets Pokemon')
    q = [
    inquirer.Text("name", message="What is your name?"),
    inquirer.List("gender", message="Gender", choices=["Girl", "Boy", "Non-Binary"], default="Girl"),
    inquirer.Checkbox(
        "nature", message="Describe your nature (Press space bar to select multiple. Enter to submit", choices=["Sassy", "Kind", "Brave", "Loyal", "Brilliant", "Romantic", "Hot-Headed", "Timid", "Quiet", "Loud", "Carefree", "Whimsical", "Rude"]
    ),
    inquirer.List("first_pokemon", message="Select your first Pokemon!", choices=["Torchic: Fire", "Fennekin: Fire", "Squirtle: Water", "Bulbasaur: Nature"], default="Bulbasaur: Nature"),
    ]
    answers = inquirer.prompt(q, theme=GreenPassion()) 
    if answers["first_pokemon"] == "Bulbasaur: Nature":
        first_pokemon = pokemon_db.bulbasaur
    elif answers["first_pokemon"] == "Fennekin: Fire":
        first_pokemon = pokemon_db.fennekin
    elif answers["first_pokemon"] == "Squirtle: Water":
        first_pokemon = pokemon_db.squirtle
    elif answers["first_pokemon"] == "Torchic: Fire":
        first_pokemon = pokemon_db.torchic

    #Create Player based on inputs
    my_player = Player(answers["name"], answers["gender"], "-_-", answers["nature"], [first_pokemon], [], 0)
    return my_player

def initialize_cpu_trainers(irange1, irange2, jrange1, jrange2, grid):
    i_cpu = random.randint(irange1, irange2)
    j_cpu = random.randint(jrange1, jrange2)
    while (grid[i_cpu][j_cpu].is_object_on_tile) or (grid[i_cpu][j_cpu].is_trainer_on_tile):
        i_cpu = random.randint(irange1, irange2)
        j_cpu = random.randint(jrange1, jrange2)
    return i_cpu, j_cpu


def battle(my_player: Player, trainer_opponent: CPU_Trainer):
    #have trainer pick random pokemon to start
    trainer_pokemon = random.choice(trainer_opponent.pokemon_list)
    #choose a pokemon to start for battle   
    q = [
        inquirer.List("pokemon", message="Select your Pokemon to use in Battle!", choices=[i.name for i in my_player.pokemon_list]),
    ]
    answers = inquirer.prompt(q, theme=GreenPassion()) 
    my_pokemon =  answers['pokemon']
    for pokemon in my_player.pokemon_list:
        if pokemon.name == my_pokemon:
            my_pokemon = pokemon
            break
    print(f"You have chosen {my_pokemon.name} to go into battle!\n Nature: {my_pokemon.nature}, Health: {my_pokemon.health}\n {my_pokemon.pokemon_display}")
    print(f"You will be battling {trainer_pokemon.name} Nature: {trainer_pokemon.nature}, Health: {trainer_pokemon.health}\n {trainer_pokemon.pokemon_display}")

    battle = True
    while battle:
        print(f'My Pokemon Health: {my_pokemon.health}  |  Opponent Pokemon Health: {trainer_pokemon.health}')
        questions = [
            inquirer.List("Battle", message="Battle Options", choices=['RUN', 'FIGHT', 'CHANGE POKEMON', 'USE ITEM']),
        ]
        answers2 = inquirer.prompt(questions, theme=GreenPassion())
        #Run
        if answers2["Battle"] == 'RUN':
            print("Running Away!")
            battle = False
            return
     
        #Fight
        if answers2["Battle"] == 'FIGHT':
            attack_question = [
            inquirer.List("attack", message="Select you attack", choices=[i.name for i in my_pokemon.attacks]),
            ]
            answers3 = inquirer.prompt(attack_question, theme=GreenPassion())
            my_attack = None
            for attack in my_pokemon.attacks:
                if attack.name == answers3['attack']:
                    my_attack = attack
                    break

            print(f"Attacking with {my_attack.name}, Strength: {my_attack.strength}, Opponent {trainer_pokemon.name} has lost {my_attack.strength} health!")
            #Decrease Trainer Pokemon Health
            trainer_pokemon.health -= my_attack.strength
            #Check if Trainer Pokemon Health is <= 0
            if (trainer_pokemon.health <= 0):
                no_available_pokemon = True #flag for if all pokemon have been defeated
                #Trainer trying to find another pokemon to fight with
                for pokemon in trainer_opponent.pokemon_list:
                    if pokemon.health > 0:
                        print(f"{trainer_pokemon.name} has lost all its health!\n {trainer_opponent.name} switches pokemon to {pokemon.name} Nature: {pokemon.nature}, Health: {pokemon.health}\n {pokemon.pokemon_display}")
                        trainer_pokemon = pokemon
                        no_available_pokemon = False #found a pokemon with > 0 health
                        break
                #You win if all of the Trainer's Pokemon have <= 0 health
                if no_available_pokemon:
                    print('You Won the Battle!')
                    print(f"You have recieved ${trainer_opponent.money_to_win} and Pokemon {trainer_opponent.pokemon_to_win.name}, Nature: {trainer_opponent.pokemon_to_win.nature}!\n{trainer_opponent.pokemon_to_win.pokemon_display}")
                    my_player.pokemon_list.append(copy.deepcopy(trainer_opponent.pokemon_to_win))
                    my_player.money += trainer_opponent.money_to_win
                    trainer_opponent.pokemon_list.remove(trainer_opponent.pokemon_to_win)
                    battle = False
                    input("Press Enter to return to the Map!")
                    return "WON"
            #Trainer Pokemon attacks your Pokemon
            trainer_attack = random.choice(trainer_pokemon.attacks)
            print(f"Trainer Attacked using {trainer_attack.name}. {my_pokemon.name} has lost {trainer_attack.strength} health")

            #Decrement health
            my_pokemon.health -= trainer_attack.strength
    
            if (my_pokemon.health <= 0):
                no_available_pokemon = True #flag for if all pokemon have been defeated
                #Checking if all pokemon 
                for pokemon in my_player.pokemon_list:
                    if pokemon.health > 0:
                        print(f"{my_pokemon.name} has lost all its health! {my_pokemon.name} Choose a new Pokemon!")
                        no_available_pokemon = False #found a pokemon with > 0 health
                        break

                #You win if all of the Trainer's Pokemon have <= 0 health
                if no_available_pokemon:
                    print('You Lost Game!!')
                    battle = False
                    input("Press Enter to end the game!")
                    return "LOST"

        #Change Pokemon
        if answers2["Battle"] == 'CHANGE POKEMON':
            #choose a pokemon to start for battle   
            pokemon = [
                inquirer.List("pokemon", message="Select your Pokemon to use in Battle!", choices=[i.name for i in my_player.pokemon_list]),
            ]
            answers3 = inquirer.prompt(pokemon, theme=GreenPassion()) 
            my_pokemon =  answers3['pokemon']
            for pokemon in my_player.pokemon_list:
                if pokemon.name == my_pokemon:
                    my_pokemon = pokemon
                    break
            print(f"You have chosen {my_pokemon.name} to go into battle!\n {my_pokemon.pokemon_display} Nature: {my_pokemon.nature}, Health: {my_pokemon.health}")

        #Use Item 
        if answers2["Battle"] == 'USE ITEM':
            #choose an item
            items = [
                inquirer.List("item", message="Select your Item to use in Battle!", choices=[i.name for i in my_player.bag]),
            ]
            answers4 = inquirer.prompt(items, theme=GreenPassion()) 
            my_item =  answers4['item']
            for item in my_player.bag:
                if item.name == my_item:
                    my_item = item
                    break
            print(f"You have chosen {my_item.name} to use!\n This will effect the current selected pokemon.")
            heal = [
                inquirer.List("item", message="Do you want to proceed?", choices=['yes', 'no'], default='yes'),
            ]
            answers5 = inquirer.prompt(heal, theme=GreenPassion()) 
            if answers5['item'] == 'yes':
                if my_item.name == 'Heart':
                    my_pokemon.health += 50
                    print(f"{my_pokemon.name} has increased health by 50!")
                    my_player.bag.remove(my_item) #remove heart from bag
                else:
                    print('This item had no effect!')
            else:
                print('You chose No!')

