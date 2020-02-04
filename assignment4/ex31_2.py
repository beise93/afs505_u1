print("""You have to make some sort of baked good in a timed challenge.
Do you try #1 something simple or try #2 something slighly more complex?""")

something = input("> ")

if something == "1":
    print("You decide to bake cookies. But you're running out of time.")
    print("What do you do?")
    print("1. Put the oven as high as possible.")
    print("2. Keep calm.")

    bake = input("> ")

    if bake == "1":
        print("You incinerate the cookies and end up a loser.")
    elif bake == "2":
        print("The cookies end up perfect, but you took too long and lose anyways!")
    else:
        print(f"Well, doing {bake} is probably better.")
        print("You drop the cookies on the floor.")


elif something == "2":
    print("You think of 3 things to make.")
    print("1. Chocolate souffle.")
    print("2. Creme brulee.")
    print("3. Macarons.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your desert ends up a sad mess.")
        print("Good job!")


else:
    print("You can't think of anything else to make but your favorite pie and win!")
