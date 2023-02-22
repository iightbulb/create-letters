#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".



with open("input/names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("input/letters/starting_letter.txt", "r") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace("[name]", stripped_name)
        with open(f"output/readytosend/letter_for_{stripped_name}.txt", "w") as final_letter:
            final_letter.write(new_letter)


