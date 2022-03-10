import inquirer
from inquirer.themes import GreenPassion
from Player import Player


def new_game_setup():
    print('Pokemon Adventure: Alternate reality Zelda meets Pokemon')
    q = [
    inquirer.Text("name", message="What is your name?"),
    inquirer.List("gender", message="Gender", choices=["Girl", "Boy", "Non-Binary"], default="Girl"),
    inquirer.Checkbox(
        "nature", message="Describe your nature", choices=["Sassy", "Kind", "Brave", "Loyal", "Brilliant", "Romantic", "Hot-Headed", "Timid", "Quiet", "Loud", "Carefree", "Whimsical", "Rude"]
    ),
    inquirer.List("first_pokemon", message="Select your first Pokemon!", choices=["TORCHIC", "FENNEKIN", "SQUIRTLE", "BULBASAUR"], default="BULBASAUR"),
    ]
    answers = inquirer.prompt(q, theme=GreenPassion()) 

    #Create Player based on inputs
    my_player = Player(answers["name"], answers["gender"], "-_-", answers["nature"], [answers["first_pokemon"]], [], 0)
    return my_player