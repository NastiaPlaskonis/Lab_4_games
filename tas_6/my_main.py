import game_Lviv

kozelnytska = game_Lviv.Street('Kozelnytska st')
kozelnytska.set_description('There is a main campus of Ukrainian Catholic University.')

stryiska = game_Lviv.Street("Stryiska st")
stryiska.set_description("A long street where is Tax building located.")

franka = game_Lviv.Street("Ivana Franka st")
franka.set_description("A street named for an Ukrainian writer Ivan Franko.")

shevchenko = game_Lviv.Street("Taras Shevchenko st")
shevchenko.set_description("A street named for an Ukrainian writer Taras Shevchenko.")

krakivska = game_Lviv.Street("Krakivska st")
krakivska.set_description("There is a market with the same name.")

#  Lviv map 
# kozelnytska.link_street(stryiska)
# stryiska.link_street(kozelnytska)
stryiska.link_street(franka)
franka.link_street(stryiska)
shevchenko.link_street(krakivska)
krakivska.link_street(shevchenko)
kozelnytska.link_street(franka)
franka.link_street(kozelnytska)

# character at the Kozelnytska street
computer_virus = game_Lviv.Weapon('virus','weapon to atack bad computer systems')
student = game_Lviv.GoodCharacter('Student Petro Mozil', 'CS smart student:')
student.set_gift(computer_virus)
student.set_wish('new_computer')
kozelnytska.set_character(student)

# character at the Ivana Franka street
baseball_bat = game_Lviv.Weapon('baseball bat','a strong stick to beat someone')
old_man = game_Lviv.GoodCharacter('Old man Vasyl Ivanovych', 'grandpa, who likes playing baseball')
old_man.set_gift(baseball_bat)
old_man.set_wish('new_teeth')
franka.set_character(old_man)

# character at the Stryiska street
valuable_document = game_Lviv.Weapon('valuable document','a paper with all taxes arrears')
tax_man = game_Lviv.GoodCharacter('Tax man mr Smith', 'man, who works at the tax building')
tax_man.set_gift(valuable_document)
tax_man.set_wish('money')
stryiska.set_character(tax_man)

# character at the Krakivska street
entrepreneur = game_Lviv.BadCharacter('Entrepreneur mr Smith', 'man, who has business and has"t paid taxes for years')
entrepreneur.set_weakness('valuable_document')
krakivska.set_character(entrepreneur)

# character at the Taras Shevchenko street
prison_guy = game_Lviv.BadCharacter('Tax man mr Smith', 'man, who works at the tax building')
prison_guy.set_weakness('baseball_bat')
shevchenko.set_character(prison_guy)


backpack = ['new_computer', 'candy']
current_location = kozelnytska

dead = False

print('\n')
print(f'Your backpack is fool with {backpack}.')
while True:

    print("\n")
    current_location.get_details()

    inhabitant = current_location.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    command = input('> ')
    
    if command in ['Kozelnytska st', 'Stryiska st', 'Ivana Franka st', 'Taras Shevchenko st', 'Krakivska st']:
        # Move to the given street
        current_location = current_location.move(command)
    elif command == 'give':
        # Give the good character what he wants and receive the gift
        thing = input('What do you give me?\n> ')
        if thing in backpack:
            if thing == inhabitant.get_wish():
                backpack.remove(thing)
                backpack.append(inhabitant.get_gift().get_name())
                print(f"To thank you, I'm giving you [{inhabitant.get_gift().get_name()}] as a gift to atack bad guys.")
            else:
                print(f"It isn't what I want. Propose me a [{inhabitant.get_wish()}] and I'll give you the gift.")
                thing = input('> ')
                backpack.remove(thing)
                backpack.append(inhabitant.get_gift().get_name())
        else:
           print(f'There is no {thing} in my backpack.')
        print(f'Backpack: {backpack}')

    # elif command == 'fight':
    #     # Fight with bad character, atack him with his weakness
    #     if inhabitant in []
    else:
        print("I don't know how to " + command)



