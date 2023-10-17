#Working with dictionaries
#Create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Georgia': 'GA',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

#Create a basic set of states and cities in them
cities = {
    'CA': 'San Francisco',
    'GA': 'Atlanta',
    'OR': 'Portland',
    'NY': 'New York',
    'MI': 'Detroit',
    'FL': 'Miami'
}

#Add some more cities
cities['NY'] = 'Rochester'
cities['OR'] = 'Salem'
cities['GA'] = 'Savannah'

#print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

#print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

#Do it by using the state then cities dictionaries
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

#Print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abrev}")

#Print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

#Now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")
print('-' * 10)

#Safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

#Get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
