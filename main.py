import time, random, sys, os

starting_stats = {
    "Grape": {
        "Hp": 5,
        "Strength": 5
    },
    "Cherry": {
        "Hp": 6,
        "Strength": 4
    },
    "Blueberry": {
        "Hp": 4,
        "Strength": 6
    }
}

# characters
player = {
    "Nome": "",
    "Hp": 0,
    "Strength": 0
}

mushroom = {
    "Nome": "Mushroom",
    "Hp": 6,
    "Strength": 5
}

Melon = {
    "Nome": "Melon", 
    "Hp": 15,
    "Strength": 20   
}

AppleGang = {
    "Nome": "AppleGang",
    "Hp": 12 , 
    "Strength": 2
}

DragonFruit = {
    "Nome": "DragonFruit",
    "Hp": 7 ,
    "Strength": 8 
}

# items
OdonilRoses = {
    "Nome": "OdonilRoses",
    "Hp": 3 , 
    "Strength": 0
}

backpack={}

def addtoBackpack(item):
    backpack[item["Nome"]] = item

def printBackpack():
    for b in backpack:
        print("ᐶ" + b)
    print_stats(player)
    if backpack == [0]:
        typewriter("Your Backpack is empty...Go get some items")

def useItem(item): 
    player["Hp"] = player["Hp"] + item["Hp"]
    player["Strength"] = player["Strength"] + item["Strength"]

def typewriter(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char != "\n":
            time.sleep(0.0)
        else:            
            time.sleep(0)
    print("")        
    return None 

os.system("clear") 

def print_stats(Jogador):
    typewriter(Jogador["Nome"] + " stats:" + "\nᐶ Hp ❤ :" +  str(Jogador["Hp"])  +  "\nᐶ Strength 🗡 :" + str(Jogador["Strength"]) + "\n" )
    return None

def fight(statsA, statsB):
    NomeA = statsA["Nome"]
    HpA = statsA["Hp"]
    StrengthA = statsA ["Strength"]
    NomeB = statsB["Nome"]
    HpB = statsB["Hp"]
    StrengthB = statsB ["Strength"]
    print_stats(statsB)
    print(NomeA + " attacks " + NomeB)
    AatacaB = True

    while HpA > 0 and HpB > 0  :
        if AatacaB: 
            HpB = hit(NomeA, StrengthA, NomeB, HpB)
            AatacaB = False
        else:    
            HpA = hit(NomeB, StrengthB, NomeA, HpA)
            AatacaB = True
    return HpA       
        
def hit(NomeX, StrengthX, NomeY, HpY):
    attack = round(random.randint(0, StrengthX))
    HpY = HpY - attack 
    typewriter(NomeX + " hit for " + str(attack))
    if attack == 0 : 
        typewriter(NomeX + " missed completely...")
    elif HpY < 0 : 
        typewriter(NomeY + " Fainted") 
    else: 
        typewriter(NomeY + " stayed with " + str(HpY) + " Hp")
    return HpY

typewriter('Welcome to Fruit World')
typewriter('What is your name?') 
player["Nome"]=input()
nome = player["Nome"]
typewriter("World: Hello " + player["Nome"] + ', You must choose your character')
typewriter('ᐶ Grape 🍇 ')
typewriter("ᐶ Cherry 🍒 ")
typewriter("ᐶ Blueberry 🫐 ")
character=input()
if character == "Grape" or character == "Cherry" or  character == "Blueberry":
    player["Hp"]=starting_stats[character]["Hp"]
    player["Strength"]=starting_stats[character]["Strength"]
else:
    print("Invalid Character")
    exit()
print_stats(player)

# hist = "hist", texto, opcao(salto relativo) 
# optn = "optn", texto, (decisao 1, salto relativo), (decisao 2, salto relativo)
# luta = "luta", (player, salto relativo v), (adversario, salto relativo d)
# lvup = "lvup", aumento Hp, aumento Str

historia= [
    ["hist", 'U wake up in your bowl with the sound of an enormous melon next to you'],
    ["hist", "...."],
    ["hist", "Irritated by your lack of sleep you can't help but stare at the melon"],
    ["hist", "...."],
    ["hist", "The melon looks back at you"],
    ["hist", "...."],
    ["hist", "After 10 seconds of intense staring the melon snaps"],
    ["t", 5],
    ["hist", "Melon: WHAT ARE YOU LOOKING AT!?"],
    ["hist", "Still in shock your body is frozen and you can't help but look at him"],
    ["hist", "The melon starts to approach you with a figthing stance"],
    ["optn", "What do you do?:\nᐶ Fight Back\nᐶ Run Away",["Fight Back", 2],["Run Away", 1]],
    ["hist", "You try to escape...\nBut the melon quickly catches up to you and you are locked in a deadly fight!"],
    ["luta", [player, 1],[Melon, 2]],
    ["hist", "Incrivelmente ganhaste!\nCom o cansaço da luta adormeces no sítio...", 2],
    ["hist", "."],
    ["hist", "."],
    ["hist", "."],
    ["hist", "3 days later..."],
    ["hist", "You wake up again in a strange environment"],
    ["hist", "Wondering where you are you start looking around and u see an apple, a very green apple standing alone at the table, sharpening his blade..."],
    ["hist", "Still feeling wobbly, you get up and approach him..."],
    ["hist", nome + ": Sorry... But do you know where i am ?"],
    ["hist", "G. Apple: Yes, you're in a hospital... I found you completely flattened on the floor with an angry melon sitting near you..."],
    ["hist", "G. Apple: He shouldn't have messed with me..."],
    ["hist", "G. Apple: When i was leaving i heard your voice asking for help and realized you were still alive..."],
    ["hist", nome + ": So you brought me back here...."],
    ["hist", nome + ": But this doesn't seem like a hospital..."],
    ["hist", "G. Apple: That's because this is a hospital meant to avoid every single pineapple up there!!"],
    ["hist", nome + ": Pineapples??"],
    ["hist", "G. Apple: Don't you know about the history behind us fruits?\nG. Apple: How the pineapples stole everything from the rest of us and are now trying to govern the rest of the world??"],
    ["hist", nome + ":Well i was from a tree far far away from here but someone took me and i woke up next to that... that melon"],
    ["hist", "G. Apple: Don't worry,  we will build you up so stuff like that doesn't happen anymore"],
    ["hist", "G. Apple: But first, you should rest some more..."],
    ["hist", "A couple days later..."],
    ["hist", "After staying a couple weeks on the hospital and practicing in the gym with G. Apple your stats have raised up!"],
    ["lvup", (starting_stats[character]["Hp"] * 2) - player["Hp"], (starting_stats[character]["Strength"] * 2) - player["Strength"]],
    ["hist", "You and G.Apple leave the hospital and end up on a crop, where u must find the GREAT EVIL PINEAPPLE and bring him down!! "],
    ["hist", "G.Apple: This is where i will leave you... You must get vengeance for all of us!"],
    ["hist", "When you enter the crop you pass through various plants and beautiful species..."],
    ["hist", "Suddenly, a mushroom appears!"],
    ["optn", "Choose to Fight it or quickly turn left\nᐶ Fight\nᐶ Turn Left",["Turn Left", 2],["Fight", 1]],
    ["luta", [player, 4],[mushroom, 3]],
    ["hist", "You turned left and you wind up on a dark little house looking for refugee, inside there is a Chest! It seems weird though..."],
    ["optn", "Open it or Leave the house and go back for the mushroom?\nᐶ Open\nᐶ Leave",["Open", 7],["Leave", -2]],
    ["hist", "You died... Try Again", -7], 
    ["hist", nome + ": Finally i won my first battle!!"],
    ["hist", "You leveled up!"],
    ["lvup", 0, 2],
    ["hist", "As you walk and walk and walk through the field, u reach a crossways..."],
    ["optn", "Go Left or Right?\nᐶ Left\nᐶ Right", ["Left", 4], ["Right", 5]],
    ["hist", "BZZZzzzZZZZZ..... A bunch of bees jump out and start to sting you repeatedly!!\nJust when you start to panic the bees scram and you start feeling a lot better than before\nThey were medicinal bees !! You win 3 Health Points"],
    ["lvup", 3, 0],
    ["hist", "U go back to the same trail as before.", -4],
    ["hist", "You reached a dead end, but there is a crawl space beneath a few bushes\nDo you choose to crawl, or go back and go right?", 2],
    ["hist", "As you walk by the flowers there are a few Odonil Roses and you recognize them to be great for you health!", 6],
    ["optn", "ᐶ Crawl\nᐶ Go Back", ["Crawl", 1], ["Go Back", -2]],
    ["hist", "As soon as you get up a few apples approach you...\nYou lock eyes and assume a fighting stance, but they appear friendly, (Although also very weak).\nDo you want to fight them all, or try to talk?"],
    ["optn", "ᐶ Fight\nᐶ Talk", ["Fight", 1], ["Talk", 2]],
    ["luta", [player, 4], [AppleGang, 5]],
    ["hist", "You try to talk to them but they immediately switch expressions and try to jump you!\nYou have no choice but to fight!", -1],
    ["item", "You picked up Odonil Roses!\n(Check your backpack whenever you are making a decision by answering b)", OdonilRoses],
    ["hist", "You have found yourself in a good path but keep hearing a few weird sounds...\nAfter a while the noise suddenly stops and you become suspicious...\nA DragonFruit appears!!", 3],
    ["hist", "After walking for an hour, you have finally reached the Castle's Gate!!", 6],
    ["hist", "You died... Try Again", -25],
    ["optn", "ᐶ Fight\nᐶ Run Away", ["Fight", 1], ["Run Away", 2]],
    ["luta", [player, 3], [DragonFruit, 2]],
    ["hist", "You managed to run away...."],
    # finalizar pedaço de historia
    ["hist", "You died... Try Again", -27],
    ["lvup", 2, 3], 
    # implementar função que faça existir o Hp e a Strength no momento | E tambem max hp e max strength (also tem de aparecer no inventario)
    ["hist", "You had a good rest and got back to the trail.", -5],
    ["fim"],
]

l_actual = 0
p_actual = historia[l_actual]
while p_actual[0] != "fim" :
    if(p_actual[0]) == "hist":
        typewriter(p_actual[1])
        if (len(p_actual) > 2):
            l_actual = l_actual + p_actual[2]
        else:
            l_actual = l_actual + 1
    elif(p_actual[0]) == "optn":
        typewriter(p_actual[1])
        answer=input()
        if(answer == p_actual[2][0]):
            l_actual = l_actual + p_actual[2][1]
        elif (answer == p_actual[3][0]):
            l_actual = l_actual + p_actual[3][1]
        elif answer == "b":
            printBackpack()
        elif answer == "Use Item":
            item=input()
            useItem(backpack[item])
            print_stats(player)
        else:
            typewriter("Invalid answer. Try again")
    elif(p_actual[0]) == "luta":
        pA = p_actual[1][0]
        pB = p_actual[2][0]
        pA["Hp"] = fight(pA, pB)
        if(pA["Hp"] > 0 ):
            l_actual = l_actual + p_actual[1][1]
        else:
            l_actual = l_actual + p_actual[2][1]
        if player["Hp"] <= 0:
            player["Hp"]= starting_stats[character]["Hp"]
    elif(p_actual[0] == "t" ):
        time.sleep(p_actual[1]) 
        l_actual = l_actual + 1  
    elif(p_actual[0] == "lvup" ):
        player["Hp"]= player["Hp"] + p_actual[1]
        player["Strength"] = player["Strength"] + p_actual[2]
        print_stats(player)
        l_actual = l_actual + 1  
    elif(p_actual[0] == "item"):
        typewriter(p_actual[1])
        addtoBackpack(p_actual[2])
        l_actual = l_actual + 1

    p_actual = historia[l_actual]
