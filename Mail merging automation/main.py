placeholder = "[name]"

with open("Mail merging automation/Input/Names/invited.txt") as names_file:
    names = names_file.readlines()


with open("Mail merging automation/letters/starting_letter.txt") as invitation:
    letter_content = invitation.read()
    for name in names:
        stripped = name.strip()
        new_letter = letter_content.replace(placeholder, stripped)
        with open(f"Mail merging automation/Output/ReadyToSend/letter_for_{stripped}.txt", mode ="w") as completed_letter:
            completed_letter.write(new_letter)


