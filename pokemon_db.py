from Pokemon import Pokemon
from Pokemon import Attack
import climage
        #attack types 
        # 1. (element (water, fire, wind, earth) 
        # 2. martial_arts(puch, kick), 
        # 3. special (ice, lightening, wind_1, earth_special_1), 
#water attack
water_1 = Attack('Tidal Wave', 'water', 10)
water_2 = Attack('Rain Storm', 'water', 5)

#fire attack
fire_1 = Attack('Methane Gust', 'fire', 10)
fire_2 = Attack('Volcano Roar', 'fire', 5)

#wind attack
wind_1 = Attack('Tornado', 'wind', 10)
wind_2 = Attack('Swift Punch', 'wind', 5)

#earth attack
earth_1 = Attack('Earthquake', 'earth', 10)
earth_2 = Attack('Sandstorm', 'earth', 5)

#nature attack
nature_2 = Attack('Blossom Whip', 'grass', 5)

#Water Special
water_special_1 = Attack('Crystal Shards', 'special', 15)
water_special_2 = Attack('Northern Lights', 'special', 10)

#Fire Special
fire_special_1 = Attack('Shadow Zapper', 'special', 15)
fire_special_2 = Attack('Immediate Strike', 'special', 10)

#Earth Special
earth_special_1 = Attack('Metor Shower', 'special', 15)
earth_special_2 = Attack('Blackout', 'special', 10)

#nature special
grass_special_1 = Attack('Grass Thrasher', 'special', 15)

#Wind Special
wind_special_1 = Attack('Shaker', 'special', 15)
wind_special_2 = Attack('Violent Breeze', 'special', 10)

#martial_arts_punch
punch = Attack('Punch', 'martial_arts', 5)

#martial_arts_kick
kick = Attack('Kick', 'martial_arts', 5)

#starter pokemon (4)
bulbasaur = Pokemon("Bulbasaur", "Male", "Grass", [nature_2, kick, grass_special_1], "Grass", "Fire", 50, '\P/', climage.convert('pokemon_images/starter/bulbasaur.png', is_unicode=True, width=30))
fennekin = Pokemon("Fennekin", "Female", "Fire", [fire_2, kick, fire_special_2], "Fire", "Water", 50, '\P/', climage.convert('pokemon_images/starter/fennekin.png', is_unicode=True, width=30))
squirtle = Pokemon("Squirtle", "Male", "Water", [water_2, punch, water_special_2], "Water", "Wind", 50, '\P/', climage.convert('pokemon_images/starter/squirtle.png', is_unicode=True, width=30))
torchic = Pokemon("Torchic", "Female", "Fire", [fire_2, punch, fire_special_2], "Fire", "Water", 50, '\P/', climage.convert('pokemon_images/starter/torchic.png', is_unicode=True, width=30))

#water pokemon (4)
buizel = Pokemon("Buizel", "Male", "Water", [water_1, kick, water_special_2], "Water", "Wind", 80, '\P/', climage.convert('pokemon_images/water/buizel.png', is_unicode=True, width=30))
drizzle = Pokemon("Drizzle", "Female", "Water", [water_2, kick, water_special_2], "Water", "Wind", 50, '\P/', climage.convert('pokemon_images/water/drizzle.png', is_unicode=True, width=30))
mudkip = Pokemon("Mudkip", "Male", "Water", [water_2, punch, water_special_1], "Water", "Wind", 50, '\P/', climage.convert('pokemon_images/water/mudkip.png', is_unicode=True, width=30))
poliwhirl = Pokemon("Poliwhirl", "Female", "Water", [water_1, punch, water_special_1], "Water", "Wind", 80, '\P/', climage.convert('pokemon_images/water/poliwhirl.png', is_unicode=True, width=30))

#fire pokemon (4)
flareon = Pokemon("Flareon", "Male", "Fire", [fire_1, kick, fire_special_2], "Fire", "Water", 80, '\P/', climage.convert('pokemon_images/fire/flareon.png', is_unicode=True, width=30))
fletchinder = Pokemon("Fletchinder", "Female", "Fire", [fire_2, kick, fire_special_2], "Fire", "Water", 50, '\P/', climage.convert('pokemon_images/fire/fletchinder.png', is_unicode=True, width=30))
ponyta = Pokemon("Ponyta", "Male", "Fire", [fire_2, punch, fire_special_1], "Fire", "Water", 50, '\P/', climage.convert('pokemon_images/fire/ponyta.png', is_unicode=True, width=30))
slugma = Pokemon("Slugma", "Female", "Fire", [fire_1, punch, fire_special_1], "Fire", "Water", 80, '\P/', climage.convert('pokemon_images/fire/slugma.png', is_unicode=True, width=30))

#earth/nature pokemon (4)
cubone = Pokemon("Cubone", "Male", "Earth", [earth_1, kick, earth_special_2], "Earth", "Water", 80, '\P/', climage.convert('pokemon_images/earth/cubone.png', is_unicode=True, width=30))
diglett = Pokemon("Diglett", "Female", "Earth", [earth_2, kick, earth_special_2], "Earth", "Water", 50, '\P/', climage.convert('pokemon_images/earth/diglett.png', is_unicode=True, width=30))
mudsdale = Pokemon("Mudsdale", "Male", "Earth", [earth_2, punch, earth_special_1], "Earth", "Wind", 50, '\P/', climage.convert('pokemon_images/earth/mudsdale.png', is_unicode=True, width=30))
sandshrew = Pokemon("Sandshrew", "Female", "Earth", [earth_1, punch, earth_special_1], "Earth", "Wind", 80, '\P/', climage.convert('pokemon_images/earth/sandshrew.png', is_unicode=True, width=30))

#air pokemon (4)
butterfree = Pokemon("Butterfree", "Male", "Wind", [wind_1, kick, wind_special_2], "Wind", "Earth", 80, '\P/', climage.convert('pokemon_images/wind/butterfree.png', is_unicode=True, width=30))
pidgey = Pokemon("Pidgey", "Female", "Wind", [wind_2, kick, wind_special_2], "Wind", "Earth", 50, '\P/', climage.convert('pokemon_images/wind/pidgey.png', is_unicode=True, width=30))
spearow = Pokemon("Spearow", "Male", "Wind", [wind_2, punch, wind_special_1], "Wind", "Grass", 50, '\P/', climage.convert('pokemon_images/wind/spearow.png', is_unicode=True, width=30))
tornadus = Pokemon("Sandshrew", "Female", "Wind", [wind_1, punch, wind_special_1], "Wind", "Earth", 80, '\P/', climage.convert('pokemon_images/wind/tornadus.png', is_unicode=True, width=30))


#array of each pokemon by nature
starter_list = [bulbasaur, fennekin, squirtle, torchic]

water_list = [buizel, drizzle, mudkip, poliwhirl]

fire_list = [flareon, fletchinder, ponyta, slugma]

earth_list = [cubone, diglett, mudsdale, sandshrew]

wind_list = [butterfree, pidgey, spearow, tornadus]

pokemon_array = [starter_list, water_list, fire_list, earth_list, wind_list]