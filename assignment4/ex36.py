from sys import exit

def reward():
    print("The villages offer you a paltry sum of gold in return for your deeds. Do you ask for more?")

    choice = input("> ")
    if "yes" in choice:
        print("Angered by your greed the villagers attack you, overwhelmed you die and your gear sold.")

    if "no" in choice:
        print("Grateful for your beneficence the villagers celebrate you as a hero.")




def necromancer_2():
    print("After vaintly dispatching the wraiths you enter the castle.")
    print("Upon entering the castle you see the necromancer who lies in wait.")
    print("Do you you use your sword or magic in combat?")

    choice = input()

    if choice == "sword":
        print("After consuming a potion you rush the necromancer and strike him down!")
        print("The villagers decide to reward you for your valor.")
        reward()
    if choice == "magic":
        print("You decide to cast a spell but it is deflected back at you!")
        dead(why)



def necromancer():
    print("Examing the outside of the castle walls you come across a portal.")
    print("Using the portal you teleport into the necromancer's dungeon!")
    print("You are immediately confronted by the necromancer.")
    print("Do you use your sword or magic in combat?")
    magic = False

    while True:
        choice = input("> ")

        if choice == "sword":
            dead("You vainly fight against the necromancer but are overwhelmed.")
        elif choice == "magic" and not magic:
            print("Quickly thinking you cast a spell. Inicerating the evil being!")
            print("The villagers decided to reward you for your valor.")
            magic = True
            reward()
        elif choice == "magic" and magic:
            print("Quickly thinking you cast a spell but end up exploding yourself!")
        elif choice == magic:
            reward()
        else:
            print("You paused the story!!")



def wraiths():
    print("Foolhardy you take the main entrance but come across a horde of wraiths.")
    print("The wraiths screech and begin to move toward you.")
    print("Do you use the holy grenade of Antioch or charge with sword in hand?")

    choice = input("> ")

    if "sword" in choice:
        necromancer_2()
    if "grenade" in choice:
        dead("Maladroitly, you fumble the grenade and blow yourself up!")
    else:
        wraiths()

def dead(why):
    print(why, "The village is doomed!")
    exit(0)



def start():
    print("You are a wandering witch hunter tasked with monsterslaying.")
    print("A village has contracted with you to solve a series of disturbances.")
    print("The disturbances seem to come from a ruined castle.")
    print("Arriving at the castle, you have two choices: go through the main entrance or find another way in.")
    print("Which do you choose?")

    choice = input("> ")

    if "entrance" in choice:
        wraiths()
    elif "way" in choice:
        necromancer()
    else:
        dead("Struggling to decide what to do you return to the village with a false story that the villagers don't believe.")


start()
