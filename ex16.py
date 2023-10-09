from sys import argv

script, filename = argv

def backup_file(filename):
    print("We're going to backup your file.")
    backup_file_name = "backup_" + filename

    target = open(filename)
    original_file_contents = target.read()
    target.close()

    backup_target = open(backup_file_name, 'x')
    backup_target.write(original_file_contents)
    backup_target.close()
    print("We've backed up your file.")


def replace_file(filename):
    print(f"We're going to erase {filename}.")
    print("If you don't want that, hit CTRL-C (^C).")
    print("If you do want that, hit RETURN.")

    input("?")

    print("Opening the file...")
    target = open(filename, 'w')
    print("Truncating the file.  Goodbye!")
    target.truncate()

    print("Now I'm going to ask you for three lines.")

    line1 = input("line 1: ")
    line2 = input("line 2: ")
    line3 = input("line 3: ")

    print("I'm going to write these to the file.")

    target.write(line1)
    target.write("\n")
    target.write(line2)
    target.write("\n")
    target.write(line3)
    target.write("\n")

    print("And finally, we close it.")
    target.close()

backup_file(filename)
replace_file(filename)
