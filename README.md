# README
#Savana Hughes 23798928
#March 10th, 2022
#Advanced Python Pokemon Game

Notes on Implementations:
SUMMARY: 
My Pokemon game is a mix of Zelda (my favorite game series from childhood, I've played almost all) and what I know about Pokemon from friends/research (I can't believe I've never played! I think I'd enjoy it!)

I created the 4 required classes: Player, Pokemon, CPU-Trainers, and the Grid. In addition I added on an Item, Attack, and Terrain class. I also created the two required functions game start called New Game setup and the Battle function.

I used PNG files to create the gird terrain colors. I also made it so that certain terrian is inaccessessible unless a speceial item is in your bag! For example: You need the Mysterious Mountain Boots to enter Volcanic Mountain so that you can walk on Lava. 

You move by pressing WSDA keys and you can open a menu that gives you options to see whats in your bag and what pokemon you currently have.

There are 8 hearts that populate the map, all with one time use and gives your pokemon +50 health if used during battle. 

To win the game you must capture 4 pokemon of different Natures. 
To Loose the game you must have all your pokemon be defeated in battle (have health <=0)

To win a battle and gain a pokemon, you must defeat all of that trainers pokemon. After the battle, the trainer will disapear from the map. 

At first, You can only move in your Starting Grassy area and the Viridian Forest. You must collect the needed items to expand the map. 

FUTURE IMPLEMENTATION IDEAS:
In the future, I'd like to expand the game by making the battle system smarter. I made it so that each pokemon has an element they are weak to and an element they are resistant to, but I did not implement that in the battle system due to lack of time. I'd also like to add more interactions. In the middle left grass quandrant I had planned to put a town. I want to add stores to buy supplies and NPCs to interact with. Maybe a Hospital to heal pokemon!

Have fun playing!!


HOW TO RUN:

To begin create and activate the virtual environment if it doesn't already exist.

This creates the virtual environment

```
$ python3 -m venv pokemon
```

This activates the virtual environment

```
$ source pokemon/bin/activate
```

This installs the dependencies in the virtual environment

```
$ pip install -r requirements.txt
```

If you get an error: 
set the path

```
$ PATH="/usr/local/opt/icu4c/sbin:/usr/local/opt/icu4c/bin:$PATH"
```

Then run:

```
$ pip install pyicu

```

Then run this again:

```
$ pip install -r requirements.txt

```

---

In the future, you'll only have to activate the virtual environment with:
```
$ source pokemon/bin/activate

---


```

