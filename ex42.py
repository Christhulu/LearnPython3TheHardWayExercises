## Animal is-a object (yes, sort of confusing) look at the extra credit
## Highlighting the difference between is-a and has-a relationships in classes/objects
class Animal(object):
    def __init__(self, name):
        ## Animal has-a name
        self.name = name

    #The "official" string representation of an object,
    #Preferably, this is supposed to look like a valid Python expression to recreate it
    def __repr__(self):
        return "Animal()"

    #A nicely printable string representation of an object
    def __str__(self):
        return "member of Animal"

## Dog is-a(n) Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

    #The "official" string representation of an object,
    #Preferably, this is supposed to look like a valid Python expression to recreate it
    def __repr__(self):
        return "Dog()"

    #A nicely printable string representation of an object
    def __str__(self):
        return "member of Dog"

## Cat is-a(n) Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

    #The "official" string representation of an object,
    #Preferably, this is supposed to look like a valid Python expression to recreate it
    def __repr__(self):
        return "Cat()"

    #A nicely printable string representation of an object
    def __str__(self):
        return "member of Cat"

## Person is-a(n) object
class Person(object):

    def __init__(self, name, pets):
        ## Person has-a name
        self.name = name

        ## Person has-many pets of some kind
        self.pets = pets if pets else []

    #The "official" string representation of an object,
    #Preferably, this is supposed to look like a valid Python expression to recreate it
    def __repr__(self):
        return "Person()"

    #A nicely printable string representation of an object
    def __str__(self):
        return "member of Person"

    #prints in miles by default, if false, prints in kilometers
    def walk(distance:float, metric: bool):

        if metric:
            print("{self.name} has walked {kilometers} kilometers.")
        else:
            kilometers = distance / 1.609
            print("{self.name} has walked {self.distance} miles.")

## Employee
class Employee(Person):

    def __init__(self, name, pets, salary):
        ## ?? hmm what is this strange magic?
        ## This is calling the parent class (Person)'s constructor to define employee's name
        super().__init__(name, pets)
        ## Employee has-a salary
        self.salary = salary

    #The "official" string representation of an object,
    #Preferably, this is supposed to look like a valid Python expression to recreate it
    def __repr__(self):
        return "Employee()"

    #A nicely printable string representation of an object
    def __str__(self):
        return "member of Employee"

    def work_for_years(years: float):
        print("{self.name} has worked for {self.salary} years and earned {self.salary * years}.")

## Fish is-a object
class Fish(object):
    #Fish has-a name
    def __init__(self, name):
        self.name = name

    #The "official" string representation of an object,
    #Preferably, this is supposed to look like a valid Python expression to recreate it
    def __repr__(self):
        return "Fish()"

    #A nicely printable string representation of an object
    def __str__(self):
        return "member of Fish"

## Salmon is-a Fish
class Salmon(Fish):

    def __init__(self, name, swim_speed, color):
        super().__init__(name)

        self.swim_speed = swim_speed
        self.color = color
        self.texture = "Moist, Tender"
        self.flavor = "Rich, Buttery"

    #The "official" string representation of an object,
    #Preferably, this is supposed to look like a valid Python expression to recreate it
    def __repr__(self):
        return "Salmon()"

    #A nicely printable string representation of an object
    def __str__(self):
        return "member of Salmon"

    def swim_for_distance(distance: float, metric: bool):
        if metric:
            print("{self.name} has walked {kilometers} kilometers.")
        else:
            kilometers = distance / 1.609
            print("{self.name} has walked {self.distance} miles.")

## Halibut is-a Fish
class Halibut(Fish):
    def __init__(self, name, swim_speed, color):
        super().__init__(name)
        self.swim_speed = swim_speed
        self.color = color
        self.texture = "Firm, Flaky"
        self.flavor = "Mild, Sweet"

    #The "official" string representation of an object,
    #Preferably, this is supposed to look like a valid Python expression to recreate it
    def __repr__(self):
        return "Halibut()"

    #A nicely printable string representation of an object
    def __str__(self):
        return "member of Halibut"

    def swim_for_distance(distance: float, metric: bool):
        if metric:
            print("{self} has walked {kilometers} kilometers.")
        else:
            kilometers = distance / 1.609
            print("{self} has walked {self.distance} miles.")

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary", [satan])

## frank is-a(n) Employee
frank = Employee("Frank", 120000, [rover])

## flipper is-a Fish
flipper = Fish("flipper")

print(flipper)

# ## crouse is-a Salmon
crouse = Salmon("crouse", 42, "silver")

# ## harry is-a Halibut
harry = Halibut("harry", 42, "brown")
