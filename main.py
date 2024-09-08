#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt

with open("Input/Names/invited_names.txt") as invited:
    names = invited.readlines()
    print(names)
with open("Input/Letters/starting_letter.txt", 'r') as letter:
    contents = letter.read()

    for name in names:
        new_name = name.strip()
        new_letter = contents.replace("[name]", new_name)

        # Save the letters in the folder "ReadyToSend".
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", 'w') as output:
            output.write(new_letter)

