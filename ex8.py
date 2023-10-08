
#Create a formatter with 4 blocks that we can sub variables into
formatter = "{} {} {} {}"


#Each of these lines has 4 items to substitute into our formatter variable by calling
#its format function
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
#Even if we set them on new lines, it still works the same way
print(formatter.format(
    "I am",
    "trying to format",
    "some text in a cool",
    "way"
))
