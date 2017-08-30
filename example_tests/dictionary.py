# create a mapping of state to abbreviation
states = [
    {
    "Oregon": "OR",
    "Florida": "FL",
    "California": "CA",
    "New York": "NY",
    "Michigan": "MI"
    }
]

# create a basic set of states and some cities in them
cities = [
    {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
    }
]

five_states = states[0:5]

print five_states
# add some more cities
#cities['NY'] = 'New York'
#cities['OR'] = 'Portland'

### print out some cities
##print '- ' * 10
##print "NY State has: ", cities['NY']
##print "OR State has: ", cities['OR']

### List Comprehension ###

a = [ {'name':'pippo', 'age':'5'} , {'name':'pluto', 'age':'7'} ]
print a
l_comprehension = [d for d in a if d['name'] == 'pluto']
print(l_comprehension)
print(l_comprehension[0])

diction = l_comprehension[0]

print("\nHere's a planet name: " + diction['name'])

print(a[0:1])

# nesting the list of dictionaries in a dictionary
# you end up with a dictionary with a list with dictionaries...
dictionary = {}
dictionary['streams'] = a[0:2]
print dictionary


#My dictionary
dict = {}
dict['Capital']="London"
dict['Food']="Fish&Chips"
dict['2012']="Olympics"

#lists
temp = []
dictList = []

for key, value in dict.iteritems():
    temp = [key,value]
    dictList.append(temp)
