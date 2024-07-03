all_pokemon = {}

advantage = {"Bug": ["Grass", "Dark", "Psychic"], "Dark": ["Ghost", "Psychic"], "Dragon": "Dragon", "Electric": ["Flying", "Water"], "Fairy": ["Fighting", "Dark", "Dragon"], "Fighting": ["Dark", "Ice", "Normal", "Rock", "Steel"], "Fire": ["Bug", "Grass", "Ice", "Steel"], "Flying": ["Bug", "Fighting", "Grass"], "Ghost": ["Ghost", "Psychic"], "Grass": ["Ground", "Rock", "Water"], "Ground": ["Electric", "Fire", "Poison", "Rock", "Steel"], "Ice": ["Dragon", "Flying", "Grass", "Ground"], "Normal": [], "Poison": ["Fairy", "Grass"], "Psychic": [], "Rock": ["Bug", "Fire", "Flying", "Ice"], "Steel": ["Fairy", "Ice", "Rock"], "Water": ["Fire", "Ground", "Rock"]}
resistance = {"Bug": ["Grass", "Fighting", "Ground"], "Dark": ["Ghost", "Dark"], "Dragon": ["Fire", "Water", "Electric", "Grass"], "Electric": ["Electric", "Flying", "Steel"], "Fairy": ["Fighting", "Bug", "Dark"], "Fighting": ["Bug", "Rock", "Dark"], "Fire": ["Fire", "Grass", "Ice", "Bug", "Steel", "Fairy"], "Flying": ["Grass", "Fighting", "Bug"], "Ghost": ["Poison", "Bug"], "Grass": ["Water", "Electric", "Grass", "Ground"], "Ground": ["Poison", "Rock"], "Ice": ["Ice"], "Normal": [], "Poison": ["Grass", "Fighting", "Poison", "Bug", "Fairy"], "Psychic": ["Fighting", "Psychic"], "Rock": ["Normal", "Fire", "Poison", "Flying"], "Steel": ["Normal", "Grass", "Ice", "Flying", "Psychic", "Bug", "Rock", "Dragon", "Steel", "Fairy"], "Water": ["Fire", "Water", "Ice", "Steel"]}
immunity = {"Bug": [], "Dark": ["Psychic"], "Dragon": [], "Electric": [], "Fairy": ["Dragon"], "Fighting": [], "Fire": [], "Flying": ["Ground"], "Ghost": ["Normal", "Fighting"], "Grass": [], "Ground": ["Electric"], "Ice": [], "Normal": ["Ghost"], "Poison": [], "Psychic": [], "Rock": [], "Steel": ["Poison"], "Water": []}

class Pokemon:
    def __init__(self, name, level, type):
      self.name = name
      self.level = level
      self.type = type
      self.health = level * 5
      self.max_health = level * 5
      self.is_knocked_out = False
      all_pokemon[self.name] = self

    def __repr__(self):
      return "{name} is a level {level} {type} type Pokemon, who currently has {health} hitpoints.".format(name = self.name, level = self.level, type = self.type, health = self.health)

    def attack(attacker, defender):
      if attacker.is_knocked_out:
        print("{name} is unconscious and can not attack!".format(name = attacker.name))
        return
      multiplyer = 1
      effectiveness = ""
      if attacker.type in immunity[defender.type]:
        multiplyer = 0
        effectiveness = defender.name + " is immune to " + attacker.type + " type attacks!"
      if defender.type in advantage[attacker.type]:
        multiplyer = 2
        effectiveness = "It's super effective!"
      if attacker.type in resistance[defender.type]:
        multiplyer = 0.5
        effectiveness = "It's not very effective..."
      print("{attacker} attacked {defender} for {damage} damage!".format(attacker = attacker.name, defender = defender.name, damage = attacker.level * multiplyer))
      print(effectiveness)    
      defender.lose_health(attacker.level * multiplyer)          
    
    def lose_health(self, amount):
      self.health -= amount
      if self.health <= 0:
        self.health = 0
        self.knock_out()
      else:
        print("{pokemon} has {health} hitpoints left".format(pokemon = self.name, health = self.health))

    def knock_out(self):
      self.is_knocked_out = True
      if self.health != 0:
        self.health = 0
      print("{name} has fainted!".format(name = self.name))

    def revive(self):
      self.is_knocked_out = False
      if self.health == 0:
        self.health == 1
      print("{name} has been revived!".format(name = self.name))

    def gain_health(self, amount):
      if self.health == 0:
        self.revive()
      self.health += amount
      if self.health > self.max_health:
        self.health = self.max_health
      print("{name} now has {amount} hitpoints.".format(name = self.name, amount = self.health))
      

class Trainer:
    def __init__(self, title, name, pokemon_team, num_potions):
      self.title = title
      self.name = name
      self.pokemon_team = pokemon_team
      self.num_potions = num_potions
      self.active_pokemon = 0

    def __repr__(self):
      print("{title} {name} has the following pokemon:".format(title = self.title, name = self.name))
      for pokemon in self.pokemon_team:
        print(pokemon)
      return "{name}'s current active pokemon is {pokemon}".format(name = self.name, pokemon = self.pokemon_team[self.active_pokemon].name)

    def attack_opponent(self, opponent):
      attacker = self.pokemon_team[self.active_pokemon]
      defender = opponent.pokemon_team[opponent.active_pokemon]
      attacker.attack(defender)

    def use_potion(self):
        if self.num_potions > 0:
            print("You used a potion on {name}.".format(name = self.pokemon_team[self.active_pokemon].name))
            self.pokemon_team[self.active_pokemon].gain_health(20)
            self.num_potions -= 1
      
    def switch_active(self, new_active):
      if new_active < len(self.pokemon_team) and new_active >= 0:
        if self.pokemon_team[new_active].is_knocked_out:
          print("{name} has fainted and is unable to battle...".format(name = self.pokemon_team[new_active].name))
        elif new_active == self.active_pokemon:
          print("{name} is already out...".format(name = self.pokemon_team[new_active].name))
        else:
          self.active_pokemon = new_active
          print("Go {name}, it's your turn!".format(name = self.pokemon_team[self.active_pokemon].name))

bulbasaur = Pokemon("Bulbasaur", 5,  "Grass")
ivysaur = Pokemon("Ivysaur", 5, "Grass")
venasaur = Pokemon("Venasaur", 5,  "Grass")
charmander = Pokemon("Charmander", 5, "Fire")
charmeleon = Pokemon("Charmeleon", 5, "Fire")
charizard = Pokemon("Charizard", 5, "Fire")
squirtle = Pokemon("Squirtle", 5, "Water")
wartortle = Pokemon("Wartortle", 5, "Water")
blastoise = Pokemon("Blastoise", 5, "Water")
caterpie = Pokemon("Caterpie", 5, "Bug")
metapod = Pokemon("Metapod", 5, "Bug")
butterfree = Pokemon("Butterfree", 5, "Bug")
weedle = Pokemon("Weedle", 5, "Bug")
kakuna = Pokemon("Kakuna", 5, "Bug")
beedrill = Pokemon("Beedrill", 5, "Bug")
pidgey = Pokemon("Pidgey", 5, "Normal")
pidgeotto = Pokemon("Pidgeotto", 5, "Normal")
pidgeot = Pokemon("Pidgeot", 5, "Normal")
rattata = Pokemon("Rattata", 5, "Normal")
raticate = Pokemon("Raticate", 5, "Normal")
spearow = Pokemon("Spearow", 5, "Normal")
fearow = Pokemon("Fearow", 5, "Normal")
ekans = Pokemon("Ekans", 5, "Poison")
arbok = Pokemon("Arbok", 5, "Poison")
pikachu = Pokemon("Pikachu", 5, "Electric")
raichu = Pokemon("Raichu", 5, "Electric")
sandshrew = Pokemon("Sandshrew", 5, "Ground")
sandslash = Pokemon("Sandslash", 5, "Ground")
nidoranf = Pokemon("Nidoran(Female)", 5, "Poison")
nidorina = Pokemon("Nidorina", 5, "Poison")
nidoqueen = Pokemon("Nidoqueen", 5, "Poison")
nidoranm = Pokemon("Nidoran(Male)", 5, "Poison")
nidorino = Pokemon("Nidorino", 5, "Poison")
nidoking = Pokemon("Nidoking", 5, "Poison")
clefairy = Pokemon("Clefairy", 5, "Fairy")
clefable = Pokemon("Clefable", 5, "Fairy")
vulpix = Pokemon("Vulpix", 5, "Fire")
ninetails = Pokemon("Ninetails", 5, "Fire")
jigglypuff = Pokemon("Jigglypuff", 5, "Normal")
wigglytuff = Pokemon("Wigglytuff", 5, "Normal")
zubat = Pokemon("Zubat", 5, "Poison")
golbat = Pokemon("Golbat", 5, "Poison")
oddish = Pokemon("Oddish", 5, "Grass")
gloom = Pokemon("Gloom", 5, "Grass")
vileplume = Pokemon("Vileplume", 5, "Grass")
paras = Pokemon("Paras", 5, "Bug")
parasect = Pokemon("Parasect", 5, "Bug")
venonat = Pokemon("Venonat", 5, "Bug")
venomoth = Pokemon("Venomoth", 5, "Bug")
diglett = Pokemon("Diglett", 5, "Ground")
dugtrio = Pokemon("Dugtrio", 5, "Ground")
meowth = Pokemon("Meowth", 5, "Normal")
persian = Pokemon("Persian", 5, "Normal")
psyduck = Pokemon("Psyduck", 5, "Water")
golduck = Pokemon("Golduck", 5, "Water")
mankey = Pokemon("Mankey", 5, "Fighting")
primeape = Pokemon("Primeape", 5, "Fighting")
growlithe = Pokemon("Growlithe", 5, "Fire")
arcanine = Pokemon("Arcanine", 5, "Fire")
poliwag = Pokemon("Poliwag", 5, "Water")
poliwhirl = Pokemon("Poliwhirl", 5, "Water")
poliwrath = Pokemon("Poliwrath", 5, "Water")
abra = Pokemon("Abra", 5, "Psychic")
kadabra = Pokemon("Kadabra", 5, "Psychic")
alakazam = Pokemon("Alakazam", 5, "Psychic")
machop = Pokemon("Machop", 5, "Fighting")
machoke = Pokemon("Machoke", 5, "Fighting")
machamp = Pokemon("Machamp", 5, "Fighting")
bellsprout = Pokemon("Bellsprout", 5, "Grass")
weepinbell = Pokemon("Weepinbell", 5, "Grass")
victreebel = Pokemon("Victreebel", 5, "Grass")
tentacool = Pokemon("Tentacool", 5, "Water")
tentacruel = Pokemon("Tentacruel", 5, "Water")
geodude = Pokemon("Geodude", 5, "Rock")
graveler = Pokemon("Graveler", 5, "Rock")
golem = Pokemon("Golem", 5, "Rock")
ponyta = Pokemon("Ponyta", 5, "Fire")
rapidash = Pokemon("Rapidash", 5, "Fire")
slowpoke = Pokemon("Slowpoke", 5, "Water")
slowbro = Pokemon("Slowbro", 5, "Water")
magnemite = Pokemon("Magnemite", 5, "Electric")
magneton = Pokemon("Magneton", 5, "Electric")
farfetchd = Pokemon("Farfetch'd", 5, "Normal")
doduo = Pokemon("Doduo", 5, "Normal")
dodrio = Pokemon("Dodrio", 5, "Normal")
seel = Pokemon("Seel", 5, "Water")
dewgong = Pokemon("Dewgong", 5, "Water")
grimer = Pokemon("Grimer", 5, "Poison")
muk = Pokemon("Muk", 5, "Poison")
shellder = Pokemon("Shellder", 5, "Water")
cloyster = Pokemon("Cloyster", 5, "Water")
gastly = Pokemon("Gastly", 5, "Ghost")
haunter = Pokemon("Haunter", 5, "Ghost")
gengar = Pokemon("Gengar", 5, "Ghost")
onix = Pokemon("Onix", 5, "Rock")
drowzee = Pokemon("Drowzee", 5, "Psychic")
hypno = Pokemon("Hypno", 5, "Psychic")
krabby = Pokemon("Krabby", 5, "Water")
kingler = Pokemon("Kingler", 5, "Water")
voltorb = Pokemon("Voltorb", 5, "Electric")
electrode = Pokemon("Electrode", 5, "Electric")
exeggcute = Pokemon("Exeggcute", 5, "Grass")
exeggutor = Pokemon("Exeggutor", 5, "Grass")
cubone = Pokemon("Cubone", 5, "Ground")
marowak = Pokemon("Marowak", 5, "Ground")
hitmonlee = Pokemon("Hitmonlee", 5, "Fighting")
hitmonchan = Pokemon("Hitmonchan", 5, "Fighting")
lickitung = Pokemon("Lickitung", 5, "Normal")
koffing = Pokemon("Koffing", 5, "Poison")
weezing = Pokemon("Weezing", 5, "Poison")
rhyhorn = Pokemon("Rhyhorn", 5, "Ground")
rhydon = Pokemon("Rhydon", 5, "Ground")
chansey = Pokemon("Chansey", 5, "Normal")
tangela = Pokemon("Tangela", 5, "Grass")
kangaskhan = Pokemon("Kangaskhan", 5, "Normal")
horsea = Pokemon("Horsea", 5, "Water")
seadra = Pokemon("Seadra", 5, "Water")
goldeen = Pokemon("Goldeen", 5, "Water")
seaking = Pokemon("Seaking", 5, "Water")
staryu = Pokemon("Staryu", 5, "Water")
starmie = Pokemon("Starmie", 5, "Water")
mrmime = Pokemon("Mr. Mime", 5, "Psychic")
scyther = Pokemon("Scyther", 5, "Bug")
jynx = Pokemon("Jynx", 5, "Ice")
electabuzz = Pokemon("Electabuzz", 5, "Electric")
magmar = Pokemon("Magmar", 5, "Fire")
pinsir = Pokemon("Pinsir", 5, "Bug")
tauros = Pokemon("Tauros", 5, "Normal")
magikarp = Pokemon("Magikarp", 5, "Water")
gyarados = Pokemon("Gyarados", 5, "Water")
lapras = Pokemon("Lapras", 5, "Water")
ditto = Pokemon("Ditto", 5, "Normal")
eevee = Pokemon("Eevee", 5, "Normal")
vaporeon = Pokemon("Vaporeon", 5, "Water")
jolteon = Pokemon("Jolteon", 5, "Electric")
flareon = Pokemon("Flareon", 5, "Fire")
porygon = Pokemon("Porygon", 5, "Normal")
omanyte = Pokemon("Omanyte", 5, "Rock")
omastar = Pokemon("Omastar", 5, "Rock")
kabuto = Pokemon("Kabuto", 5, "Rock")
kabutops = Pokemon("Kabutops", 5, "Rock")
aerodactyl = Pokemon("Aerodactyl", 5, "Rock")
snorlax = Pokemon("Snorlax", 5, "Normal")
articuno = Pokemon("Articuno", 5, "Ice")
zapdos = Pokemon("Zapdos", 5, "Electric")
moltres = Pokemon("Moltres", 5, "Fire")
dratini = Pokemon("Dratini", 5, "Dragon")
dragonair = Pokemon("Dragonair", 5, "Dragon")
dragonite = Pokemon("Dragonite", 5, "Dragon")
mewtwo = Pokemon("Mewtwo", 5, "Psychic")
mew = Pokemon("Mew", 5, "Psychic")


for mon in all_pokemon:
  print(all_pokemon[mon])

trainer_one_title = input("Welcome to the wonderful world of Pokemon! Please choose a title. (Ex. Pyromaniac, Gardener, Swimmer, etc.) ")
trainer_one_name = input("And what is your name? ")
trainer_two_title = input("Trainer two, please choose a title ")
trainer_two_name = input("And what is your name? ")

#VVV FOR TESTING PURPOSES VVV
# trainer_one_title = "Pyro"
# trainer_one_name = "Zack"
# trainer_two_title = "Tidal"
# trainer_two_name = "Torie"

# team_one = [charmander, charmeleon, charizard, magmar, rapidash, arcanine]
# team_two = [squirtle, wartortle, blastoise, poliwag, poliwhirl, poliwrath]
#^^^ FOR TESTING PURPOSES ^^^

team_one = []
team_two = []

choice = input("Let's get ready for your first Pokemon battle! You will each get 6 Pokemon. " + trainer_two_title + " " + trainer_two_name + " will choose first. You may choose any Pokemon from the Kanto Region (Generation 1). Please type the name of the pokemon you would like on your team, then press enter! ")

while choice not in all_pokemon:
  choice = input("Whoops! The Pokemon you entered does not exist. Please type the name of the pokemon you would like on your team, then press enter! ")
team_two.append(all_pokemon[choice])


choice = input("Excelent choice! " + trainer_one_title + " " + trainer_one_name + " will choose next ")

while choice not in all_pokemon:
  choice = input("Whoops! The Pokemon you entered does not exist. Please type the name of the pokemon you would like on your team, then press enter! ")
team_one.append(all_pokemon[choice])

print("Excelent choice!")

turn = 1
while turn < 11:
  if turn % 2 != 0:
    choice = input(trainer_two_name + ", please select your next pokemon! ")
    while choice not in all_pokemon:
      choice = input("Whoops! The Pokemon you entered does not exist. Please type the name of the pokemon you would like on your team, then press enter! ")
    team_two.append(all_pokemon[choice])
    print("Excelent choice!")
    turn += 1
  elif turn % 2 == 0:
    choice = input(trainer_one_name + ", please select your next pokemon! ")
    while choice not in all_pokemon:
      choice = input("Whoops! The Pokemon you entered does not exist. Please type the name of the pokemon you would like on your team, then press enter! ")
    team_one.append(all_pokemon[choice])
    print("Excelent choice!")
    turn += 1

print(team_one)
print(team_two)

trainer_one = Trainer(trainer_one_title, trainer_one_name, team_one, 3)
trainer_two = Trainer(trainer_two_title, trainer_two_name, team_two, 3)

print("\n")
print("Prepare for battle! \n")
print(trainer_one)
print("\n")
print(trainer_two)
print("\n")
print("\n")

winner = "null"
loser = "null"
turn = 1

while winner == "null":
  if trainer_one.pokemon_team[0].is_knocked_out and trainer_one.pokemon_team[1].is_knocked_out and trainer_one.pokemon_team[2].is_knocked_out and trainer_one.pokemon_team[3].is_knocked_out and trainer_one.pokemon_team[4].is_knocked_out and trainer_one.pokemon_team[5].is_knocked_out:
    winner = trainer_two.name
    loser = trainer_one.name
  elif trainer_two.pokemon_team[0].is_knocked_out and trainer_two.pokemon_team[1].is_knocked_out and trainer_two.pokemon_team[2].is_knocked_out and trainer_two.pokemon_team[3].is_knocked_out and trainer_two.pokemon_team[4].is_knocked_out and trainer_two.pokemon_team[5].is_knocked_out:
    winner = trainer_one.name
    loser = trainer_two.name
  else:
    if turn % 2 != 0:
      print("It is " + trainer_one.name + "'s turn.")
      print("\n")
      action = input(trainer_one.name + ", What will you do? Your options are 'Attack', 'Use Potion', or 'Switch'. Please type your selection, then press enter. ")
      while action != "Attack" and action != "Use Potion" and action != "Switch":
        action = input("Please type 'Attack', 'Use Potion', or 'Switch', then press enter. ")
      if action == "Attack":
        active = trainer_one.pokemon_team[trainer_one.active_pokemon]
        if active.is_knocked_out:
          print("{name} is unable to battle, please select another Pokemon! ".format(name = active.name))
          print(trainer_one.pokemon_team)
          target = int(input("Which pokemon will you switch to? Enter a number from 1-6 ")) - 1
          while target < 0 or target > (len(trainer_one.pokemon_team) - 1):  
            target = int(input("Which pokemon will you switch to? Enter a number from 1-6 ")) - 1
          trainer_one.switch_active(target)
        else:
          trainer_one.attack_opponent(trainer_two)
          turn += 1
      if action == "Use Potion":
          if trainer_one.num_potions > 0:
            trainer_one.use_potion()
            print("You have {0} potions left".format(trainer_one.num_potions))
            turn += 1
          else:
            print("You are out of potions!")
      if action == "Switch":    
        print(trainer_one.pokemon_team)
        target = int(input("Which pokemon will you switch to? Enter a number from 1-6 ")) - 1
        while target < 0 or target > (len(trainer_one.pokemon_team) - 1):
          target = int(input("Which pokemon will you switch to? Enter a number from 1-6 ")) - 1
        trainer_one.switch_active(target)
      print("\n")
    elif turn % 2 == 0:
      print("It is " + trainer_two.name + "'s turn.")
      print("\n")
      action = input(trainer_two.name + ", What will you do? Your options are 'Attack', 'Use Potion', or 'Switch'. Please type your selection, then press enter. ")
      while action != "Attack" and action != "Use Potion" and action != "Switch":
        action = input("Please type 'Attack', 'Use Potion', or 'Switch', then press enter. ")
      if action == "Attack":
        active = trainer_two.pokemon_team[trainer_two.active_pokemon]
        if active.is_knocked_out:
          print("{name} is unable to battle, please select another Pokemon! ".format(name = active.name))
          print(trainer_two.pokemon_team)
          target = int(input("Which pokemon will you switch to? Enter a number from 1-6")) - 1
          while target < 0 or target > (len(trainer_two.pokemon_team) - 1):  
            target = int(input("Which pokemon will you switch to? Enter a number from 1-6")) - 1
          trainer_two.switch_active(target)
        else:
          trainer_two.attack_opponent(trainer_one)
          turn += 1
      if action == "Use Potion":
          if trainer_two.num_potions > 0:
            trainer_two.use_potion()
            print("You have {0} potions left".format(trainer_two.num_potions))
            turn += 1
          else:
            print("You are out of potions!")
      if action == "Switch":  
        print(trainer_two.pokemon_team)
        target = int(input("Which pokemon will you switch to?"))
        while target < 0 or target > (len(trainer_two.pokemon_team) - 1):
          target = int(input("Which pokemon will you switch to? Enter a number from 1-6")) - 1
        trainer_two.switch_active(target)
      print("\n")

print(loser + ", all of your pokemon have fainted! That means that " + winner + " is the winner! Congratulations on winning your first Pokemon battle!")