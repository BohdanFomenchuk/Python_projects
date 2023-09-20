pattern = '[name]'

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as file:
    letter_content = file.read()
    for name in names:
        stripped_name = name.strip()
        if pattern in letter_content:
            new_letter = letter_content.replace(pattern, stripped_name)
            with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode='w') as complete_letter:
                complete_letter.write(new_letter)
