from tracemalloc import start
from turtle import st
from CPU_Trainer import CPU_Trainer
import inquirer
from inquirer.themes import GreenPassion
from Player import Player
import pokemon_db
import random


def new_game_setup():
    print('Pokemon Adventure: Alternate reality Zelda meets Pokemon')
    q = [
    inquirer.Text("name", message="What is your name?"),
    inquirer.List("gender", message="Gender", choices=["Girl", "Boy", "Non-Binary"], default="Girl"),
    inquirer.Checkbox(
        "nature", message="Describe your nature", choices=["Sassy", "Kind", "Brave", "Loyal", "Brilliant", "Romantic", "Hot-Headed", "Timid", "Quiet", "Loud", "Carefree", "Whimsical", "Rude"]
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
    print(f"You have chosen {my_pokemon.name} to go into battle!\n {my_pokemon.pokemon_display} Nature: {my_pokemon.nature}, Health: {my_pokemon.health}")
    print(f"You will be battling {trainer_pokemon.name}\n {trainer_pokemon.pokemon_display} Nature: {trainer_pokemon.nature}, Health: {trainer_pokemon.health}")

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

            print(f"Attacking with {my_attack.name}, Strength: {my_attack.strength}")
            #
            trainer_pokemon.health -= my_attack.strength
            if (trainer_pokemon.health <= 0):
                print('You Won!')
                print(f"You have recieved {trainer_pokemon.name}, Nature: {trainer_pokemon.nature}!\n{trainer_pokemon.pokemon_display}")
                my_player.pokemon_list.append(trainer_pokemon)
                trainer_opponent.pokemon_list.remove(trainer_pokemon)
                battle = False
                return
            trainer_attack = random.choice(trainer_pokemon.attacks)
            print(f"Trainer Attacked using {trainer_attack.name}. {my_pokemon.name} has lost {trainer_attack.strength} health")
            my_pokemon.health -= trainer_attack.strength
            #have to change this to check all pokemon in inventory 
            if (my_pokemon.health <= 0):
                print('You Lost!')
                battle = False
                return

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
                    my_pokemon.health += 25
                    print(f"{my_pokemon.name} has increased health by 25!")
                else:
                    print('This item had no effect!')
            else:
                print('You chose No!')

