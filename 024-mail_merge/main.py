#TODO: Create a letter using starting_letter.txt 

# with open("./Input/Names/invited_names.txt") as name_list:
#     for name in name_list:
#         with open("./Input/Letters/starting_letter.txt", mode="r") as letter_template:
#             new_letter = letter_template.readlines()
#             new_file_name = name + ".txt"
#             f = open(new_file_name, mode="w")
#             for line in new_letter:
#                 new_lines = line.replace("[name]", name.strip())
#                 f.write(new_lines)
#             f.close()

PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as names_list:
    names = names_list.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
