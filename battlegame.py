wizard = "Wizard"
elf = "Elf"
human = "Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_damage = 150
elf_damage = 100
human_damage = 20

dragon_hp = 300
dragon_damage = 50

while True:
    print("1) Wizard")
    print("2) Elf")
    print("3) Human")
    character = input("Choose Your Character:")

    if character == "1" or character.lower() == "Wizard":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    if character == "2" or character.lower() == "Elf":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    if character == "3" or character.lower() == "Human":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
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
