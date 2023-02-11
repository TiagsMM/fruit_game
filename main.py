import time

def print_and_sleep(string, t):
    print(string)
    # time.sleep(t)
    return None

def print_stats(Who, Health, Forca ):
    print_and_sleep(Who + " stats:" + "\nᐶ Hp ❤ :" +  str(Health)  +  "\nᐶ Strength 🗡 :" + str(Forca) , 3)
    return None

print('Welcome to Fruit World')
print('What is your name?') 
nome=input()
print(nome + ', You must choose you character')
print('ᐶ Grape 🍇')
print("ᐶ Cherry 🍒")
print("ᐶ Blueberry 🫐")
character=input()
if character== "Grape":
    Hp=5
    Strength=5
elif character== "Cherry":
    Hp=7
    Strength=3
elif character== "Blueberry":
    Hp=4
    Strength=6
else:
    print("Invalid Character")
    exit()
print_stats("Your",  Hp, Strength)
print_and_sleep('U wake up in your bowl with the sound of an enormous melon next to you', 3)
print_and_sleep("....", 3)
print_and_sleep("Irritated by your lack of sleep you can't help but stare at the melon", 3)
print_and_sleep("....", 3)
print_and_sleep("The melon looks back at you", 3)
print_and_sleep("....", 5)
print_and_sleep("After 10 seconds of intense staring the melon snaps", 1)
print_and_sleep("WHAT ARE YOU LOOKING AT!?", 3)
print_and_sleep("Still in shock you're body is frozen up and you keep looking at him", 3)
print_and_sleep("The melon starts to aproach you with a figthing stance", 3)

print('What do you do?: ' )
print("ᐶ Fight Back")
print("ᐶ Run Away")
action=input()
MelonHp= 15
MelonStrength= 20
if action== "Fight Back":
    print_stats("Melon", MelonHp , MelonStrength)
elif action== "Run Away":
    print("The melon quickly catches up to you and you are locked in a deadly fight!")
    print_stats("Melon", MelonHp , MelonStrength)


