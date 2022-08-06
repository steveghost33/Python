"""
battlegame.py
Dragon Battle Roleplay
"""


def main():
    # define variables
    # ask for user input, enumerate list, provide list for user and change input from str to int
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

    character_list = [wizard, elf, human]

    for i, value in enumerate(character_list, 1):
        print("{}.) {}".format(i, value))

    character = (int(input("Choose Your Character:")))


main()
