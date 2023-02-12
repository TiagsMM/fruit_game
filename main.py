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

player = {
    "Nome": "",
    "Hp": 0,
    "Strength": 0
}

def typewriter(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char != "\n":
            time.sleep(0.05)
        else:            
            time.sleep(1)
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
    elif attack > HpY : 
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
typewriter('U wake up in your bowl with the sound of an enormous melon next to you')
typewriter("....")
typewriter("Irritated by your lack of sleep you can't help but stare at the melon")
typewriter("....")
typewriter("The melon looks back at you")
typewriter("....")
typewriter("After 10 seconds of intense staring the melon snaps")
typewriter("Melon: WHAT ARE YOU LOOKING AT!?")
typewriter("Still in shock your body is frozen and you can't help but look at him")
typewriter("The melon starts to approach you with a figthing stance")

print('What do you do?:' )
print("ᐶ Fight Back")
print("ᐶ Run Away")
action=input()

Melon= {
    "Nome": "Melon", 
    "Hp": 15,
    "Strength": 20   
}
if action== "Run Away":
    typewriter("You try to escape...\nBut the melon quickly catches up to you and you are locked in a deadly fight!")

player["Hp"] = fight(player, Melon)

typewriter(".")
typewriter(".")
typewriter(".")
typewriter("3 days later...")
typewriter("You wake up again in a strange environment")
typewriter("Wondering where you are you start looking around and u see an apple, a very green apple standing alone at the table, sharpening his blade...")
typewriter("Still feeling wobbly, you get up and approach him...")
typewriter(nome + ": Sorry... But do you know where i am ?")
typewriter("G. Apple: Yes, you're in a hospital... I found you completely flattened on the floor with an angry melon sitting near you...")
typewriter("G. Apple: He shouldn't have messed with me...")
typewriter("G. Apple: When i was leaving i heard your voice asking for help and realized you were still alive...")
typewriter(nome + ": So you brought me back here....")
typewriter(nome + ": But this doesn't seem like a hospital...")
typewriter("G. Apple: That's because this is a hospital meant to avoid every single pineapple up there!!")
typewriter(nome + ": Pineapples??")
typewriter("G. Apple: Don't you know about the history behind us fruits?\nG. Apple: How the pineapples stole everything from the rest of us and are now trying to govern the rest of the world??")
typewriter(nome + ":Well i was from a tree far far away from here but someone took me and i woke up next to that... that melon")
typewriter("G. Apple: Don't worry,  we will build you up so stuff like that doesn't happen anymore")
typewriter("G. Apple: But first, you should rest some more...")
typewriter("A couple days later...")
typewriter("After staying a couple days on the hospital and practicing in the gym with G. Apple your stats have raised up!")


if player["Hp"] < 0:
    player["Hp"]= starting_stats[character]["Hp"]

player["Hp"]= starting_stats[character]["Hp"] * 2
player["Strength"] = starting_stats[character]["Strength"] * 2


print_stats(player)

historia= {
    1: ["h", "You and G.Apple leave the hospital and end up on a crop, where u must find the GREAT EVIL PINEAPPLE and bring him down!! "],
    2: ["h", "G.Apple: This is where i will leave you... You must get vengeance for all of us!"],
    3: ["h", "When you enter the crop you pass through various plants and beautiful species..."],
    4: ["h", "Suddenly, a mushroom appears!"],
    5: ["d", "Choose to Fight or quickly Turn left?",
            ["Turn Left", 7],
            ["Fight", 6]
        ],
    6: ["l", 
            [player, 9],
            [Melon, 11]
    ],
    7: ["h", "you turned left and you wind up on a dark little house looking for refugee, inside there is a Chest! It seems weird though..."],
    8: ["d", "Open it or Leave the house?",
            ["Open", 13],
            ["Leave", 12]
    ],
    9: ["h", nome + ": Finally i won my first battle!!" ],
    10: ["u", 0, 2],
    11: ["h", "You died... Try Again", 2], 
    12: ["f"],
    13: ["h", "u died"],
    13: ["h", "welcome to 1"],
    14: ["h", "welcome to 44"],
    15: ["f"]
}

l_actual = 1
p_actual = historia[l_actual]
while p_actual[0] != "f" :
    if(p_actual[0]) == "h":
        typewriter(p_actual[1])
        if (len(p_actual) > 2):
            l_actual = p_actual[2]
        else:
            l_actual = l_actual + 1
    elif(p_actual[0]) == "d":
        typewriter(p_actual[1])
        character=input()
        if(character == p_actual[2][0]):
            l_actual = p_actual[2][1]
        elif (character == p_actual[3][0]):
            l_actual = p_actual[3][1]
        else:
            typewriter("Invalid answer. Try again")
    elif(p_actual[0]) == "l":
        pA = p_actual[1][0]
        pB = p_actual[2][0]
        pA["Hp"] = fight(pA, pB)
        if(pA["Hp"] > 0 ):
            l_actual = p_actual[1][1]
        else:
            l_actual = p_actual[2][1]
    elif(p_actual[0] == "t" ):
        time.sleep(p_actual[1]) 
        l_actual = l_actual + 1  
    elif(p_actual[0] == "u" ):
        player["Hp"]= starting_stats[character]["Hp"] + p_actual[1]
        player["Strength"] = starting_stats[character]["Strength"] + p_actual[2]
        l_actual = l_actual + 1  

    p_actual = historia[l_actual]

