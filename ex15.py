#Exercise about reading files
from sys import argv

script, filename = argv

#Open the file with that filename and hold it in the txt variable
txt = open(filename)


print(f"Here's your file {filename}")

#Print what we read out of the file
print(txt.read())

#Remember to close your file
txt.close()

print("Type the filename again:")
file_again = input("> ")

#Open the file with that filename and hold it in the txt_again variable
txt_again = open(file_again)

print(txt_again.read())

#Remember to close your file
txt_again.close()
