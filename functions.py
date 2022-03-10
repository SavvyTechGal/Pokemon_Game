import inquirer
from inquirer.themes import GreenPassion
from Player import Player
import pokemon_db


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