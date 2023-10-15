#Program for experimenting with lists
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# This first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

#Same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

#Also we can go through mixed lists too
for i in change:
    print(f"I got {i}")

#We can also build lists, first start with an empty one
elements = []
more_elements = []

# #Then use the range function to do 0 to 5 counts (note: range is not inclusive on the last value, only on the start value)
for i in range(0, 5):
    print(f"Adding {i} to the list.")
    #append is a function that lists understand
    elements.append(i)

# #now we can print them out too
for i in elements:
    print(f"Element was: {i}")

#Another way of appending items to a list, using the extend method
more_elements.extend(range(0, 20))
print("Printing more elements:")


#print more_elements
for i in more_elements:
    print(f"Element was: {i}")
