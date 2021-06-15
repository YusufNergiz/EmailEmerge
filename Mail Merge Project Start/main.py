ACEHOLDER = "[name]"
# Listed Names Of Guests
with open("./input/Names/invited_names.txt") as guest_names:
    names = guest_names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_names = name.strip()
        new_letter = letter_contents.replace(ACEHOLDER, stripped_names)
        with open(f"./output/ReadyToSend/letter_for_{stripped_names}.txt", "w") as completed_letters:
            completed_letters.write(new_letter)


