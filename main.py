# from ast import walk
# import emoji

from Grid import Grid

# converts the image to print in terminal
# inform of ANSI Escape codes[]

# output = climage.convert('pokemon_images/pokemon_wise_bear.png', is_unicode=True)
# mountain = climage.convert('terrain_images/mountain.png', is_unicode=True)
# # prints output on console.
# print(mountain)
# color = bg('#CF1020')
# print (color + " ")
# print(emoji.emojize(' :thumbs_up:'), "HI")

#Next Steps: 
# To win capture four pokemon of different types. (have earth: mountain, wind:forest, fire:desert, water:lake, special:cherry )
# Implement movement of Player if tries to move on to tile that cant walk on yet print msg ex: ("You are unable to climb Death Mountain! It has been said; however, that mystical climbing boots are hidden, somewhere in Viridian Forest.")

myGrid = Grid()
myGrid.print_grid()
myGrid.input()