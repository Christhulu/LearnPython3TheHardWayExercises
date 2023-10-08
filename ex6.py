#Create a variable named 'types_of_people' that has 2 in binary
types_of_people = 10
#Start an unfunny joke by setting it in an fstring and refer to the other variable in it
x = f"There are {types_of_people} types of people."

#Create variables for the punchline
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

#Print the joke
print(x)
print(y)

#Repeat the joke like it makes it funnier, but using new fstrings
print(f"I said: {x}")
print(f"I also said '{y}'")

#Set hilarious to a boolean value
hilarious = False

#Use this other way to format a string that already exists, and basically place it in that bracket
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

#Learn how to concatenate strings
w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
