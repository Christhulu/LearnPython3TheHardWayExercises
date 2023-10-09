#I shortened this script a lot, made things modular because that's cool
from sys import argv
from os.path import exists


def read_file(filename):
    f = open(filename, 'r').read()
    return f

def write_file(filename, data):
    f = open(filename, 'w').write(data)

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

indata = read_file(from_file)
write_file(to_file, indata)

print("Alright, all done.")
