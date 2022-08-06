def main():
    wizard = "Wizard"
    elf = "Elf"
    human = "Human"
    orc = "Orc"

    wizard_hp = 70
    elf_hp = 100
    human_hp = 150
    orc_hp = 200

    wizard_damage = 150
    elf_damage = 100
    human_damage = 20
    orc_damage = 10

    dragon_hp = 300
    dragon_damage = 50

    while True:
        print("1) Wizard")
        print("2) Elf")
        print("3) Human")
        print("4) Orc")
        print("5) Run Away")
        character = input("Choose Your Character:")

        if character.lower() == "1" or character.lower() == "wizard":
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        if character.lower() == "2" or character.lower() == "elf":
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break
        if character.lower() == "3" or character.lower() == "human":
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break
        if character.lower() == "4" or character.lower() == "orc":
            character = orc
            my_hp = orc_hp
            my_damage = orc_damage
            break
        if character.lower() == "5" or character.lower() == "Run Away":
            print("\nDid you forget your sword? Maybe next time.\n")
            quit()

        print("Unknown Character")
    print("Character:", character)
    print("Health:", my_hp)
    print("Damage:", my_damage, "\n")

    while True:
        dragon_hp = dragon_hp - my_damage
        print("The", character, "damaged the Dragon!")

        if dragon_hp <= 0:
            print("The Dragon has lost the battle", dragon_hp)
            break

        my_hp = my_hp - dragon_damage
        print("The Dragon damaged the", character)
        print("Your hitpoints are", my_hp)

        if my_hp <= 0:
            print("The", character, "has lost the battle!")
            break
        again = input("Would you like to play again? Type yes or no:")
        if again.casefold() == "yes":
            main()
        else:
            quit()


main()
