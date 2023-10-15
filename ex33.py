#While loops, plus converting some of the code to functions
numbers = []
increment_num = 1
target_num = 6

def print_range(end_number: int):
    for num in range(0, end_number):
        print(num)

def print_loop_details(end_number: int, increment_value: int, numbers = None):
    if numbers is None:
        numbers = []

    i = 0
    while i < end_number:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + increment_value
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}\n")


#Referencing what i is at the top and the bottom of the loop
print_loop_details(target_num, numbers)
print("The numbers")
print_range(target_num)
