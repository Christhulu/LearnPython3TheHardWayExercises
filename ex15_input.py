#Exercise about reading files, but passing the filename as an input
#I also added looping if they have multiple files they want to open
from sys import argv

continue_reading = True

#Open the file with that filename and hold it in the txt variable
while continue_reading:
    print("What is your filename? ")
    prompt = '> '
    filename = input(prompt)

    txt = open(filename)

    print(f"Here's your file {filename}")

    #Print what we read out of the file
    print(txt.read())

    #Remember to close your file
    txt.close()

    print(f"Do you have another file you want to open? ")
    user_input = input(prompt)
    waiting_on_user = True

    while waiting_on_user:
        if (len(user_input) == 1) and user_input.isalpha() and (user_input == 'n' or user_input == 'N'):
            continue_reading = False
            waiting_on_user = False
        elif (len(user_input) == 1) and user_input.isalpha() and (user_input == 'y' or user_input == 'Y'):
            waiting_on_user = False
        else:
            print(f"Do you have another file you want to open? ")
            user_input = input(prompt)
