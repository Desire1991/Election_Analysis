print('Hello World')
# %%
# %%
print('Hello World')

type(3)

# %%
type(ballots)
# %%
type(9999)
# %%
type(73.81)
# %%
type('hello world')
# %%
type("")
# %%
type('true')
# %%
type(True)
# %%
help('keywords')
# %%
help('keywords')
# %%
type(5+2*3)
# %%
type(5+2) = ?
# %%
type(5+2)
# %%
print(5+2*3)
# %%
print((5+2)*3)
# %%
print(8//5-3)
# %%
print((16-3)/(2+9-1))
# %%
print((3**3)%5)
# %%
print((5+9)*3/2-4)
# %%
print((5+9*3)/2-4)
# %%
print((5+3)*3)
# %%
print((5+2)*3)
# %%
print((8//5)-3)
# %%
print(8+(22*(2-4))
# %%
print(8+(22*(2-4)))
# %%
print(16-3/(2+7)-1)
# %%
print(3**(3%5))
# %%
print(5+(9*3/2-4))
# %%
print(5+(9*3/(2-4)))
# %%
>>> counties = ["Arapohoe", "Denver", "Jefferson"]
# %%
my_list = list()
>>> counties = ["Arapohoe", "Denver", "Jefferson"]

# %%
>>> counties = ["Arapohoe", "Denver", "Jefferson"]

# %%
my_list = []
counties = ['Arapahoe', 'Denver', 'Jefferson']
# %%

# %%
my_list = []
>>> counties = ["Arapahoe", "Denver", "Jefferson"]
counties

# %%
my_list = list()
>>> counties = ["Arapahoe", "Denver", "Jefferson"]
counties
# %%
>>> counties[0]
# %%
>>> counties[1]
# %%
>>> counties[2]
# %%
>>> print(counties[2])
# %%
>>> print(counties[-1]
# %%
>>> print(counties[-2])

# %%
>>> print(counties[-2])
# %%
>>> print(counties[-1])
# %%
>>> print(counties[-3])
# %%
>>> len(counties)
# %%
>>> counties(0:2)
# %%
counties(0:2)
# %%
list[start : end]
>>> counties(0:2)
# %%
>>> counties[0:2]
# %%
>>> counties[0:1]
# %%
>>> counties[:2]
# %%
>>> counties[1:]
# %%
>>> counties[1:3]
# %%
>>> counties.insert(2, "El Paso")
# %%

# %%
>>> counties.insert(2, "El Paso")
>>> counties
# %%
>>> counties.remove("El Paso")
>>> counties
# %%
>>> counties.remove("El Paso")
>>> counties

# %%
>>> counties.pop(3)
'El Paso'
>>> counties
# %%
>>> counties.insert(2: 'Jefferson')
>>> counties
# %%
>>> counties.insert(2, 'Jefferson')
>>> counties
# %%
>>> counties.remove('El Paso')
>>> counties
# %%
>>> counties[2] = "El Paso"
>>> counties
'This a Tuple'
# %%
my_tuple = tuple()
counties_tuple = ('Arapahoe', 'Denver', 'Jefferson')
# %%
>>> counties_tuple = ('Arapahoe', 'Jefferson')
>>> counties
# %%
Length of a tuple
# %%
>>> len(counties_tuple)
3
# %%
>>> counties_tuple[1]
# %%
>>> counties_tuple[2]
# %%
>>> counties_tuple[3]
# %%

# %%
>>> counties_dict = {}
>>> counties_dict["Arapahoe"] = 422829
>>> counties_dict


# %%
>>> counties_dict["Denver"] = 463353
>>> counties_dict["Jefferson"] = 432438
>>> counties_dict
# %%
>>> len(counties_dict)
# %%
>>> len(counties_dict)
# %%
print(counties_dict.items)
# %%
>>> counties_dict.items()

# %%
>>> counties_dict.key()
# %%
>>> counties_dict.keys()

# %%
>>> counties_dict.values()

# %%
>>> counties_dict.get("Denver")
# %%
>>> counties_dict.get("Denver")
# %%
>>> counties_dict.get("Arapahoe")
# %%
>>> counties_dict['Arapahoe']
# %%
>>> counties_dict["Arapahoe"]
# %%
>>> voting_data = []
>>> voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
>>> voting_data.append({"county":"Denver", "registered_voters": 463353})
>>> voting_data.append({"county":"Jefferson", "registered_voters": 432438})
>>> voting_data

# %%
>>> voting_data.insert[2, {'counties' : 'Elpaso', 'registered_voters' : 461149}]
# %%
>>> county.insert[(2, "El Paso" : "registered_voters" : 461149)]
# %%
>>> voting_data.insert({2, 'county' :'El Paso', 'registered_voters' : 461149})
>>> voting_data
# %%
>>> voting_data.insert{2, 'county' : 'El Paso', 'registered_voters' : 461149}
>>> voting_data

# %%
>>> voting_data.update( {'ElPaso' : 461149} )
>>> voting_data
# %%
>>> len(voting_data)
>>> voting_data
# %%
>>> voting_data.append("El Paso", "registred_voters" : 461149)
>>> voting_data
# %%
>>> voting_data.append("El Paso")
# %%
>>> voting_data.insert({2, 'county' : 'El Paso', 'registered_voters' : 461149})
>>> voting_data
# %%
>>> voting_data.append('El Paso', 'registered_voters' : 461149)
>>> voting_data
# %%
>>> voting_data.insert(2, 'El Paso')
>>> voting_data
# %%
>>> voting_data.remove('El Paso')
>>> voting_data
# %%
>>> voting_data.append({"county":"El Paso", "registered_voters": 461149})
>>> voting_data
# %%
>>> len(voting_data)
>>> voting_data
# %%
counties = ['Arapahoe', 'Denver', 'Jefferson']
if counties[1] == 'Denver':
    print(counties[1])


# %%
temperature = int(input('what is the temperature outside?'))

if temperature > 80:
    print('Turn on the AC.')

else:
    print('Open the windows.')
# %%
#What is your score?
score = int(input('What is your score?'))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('your grade is a B.')
    else:
        if score >= 70:
            print('your grade is a C.')
        else:
            if score >= 60:
                print('your grade is an D.')
            else:
                print('your grade is an F.')

            

# %%
# What is the score?
score = int(input('what is your test score?'))

# Determine the grade.
if score >= 90:
    print('Your score is an A.')
elif score >= 80:
    print('Your grade is an B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F')
# %%

# Membership operators

counties = ['Arapahoe', 'Denver', 'Jefferson'] 
if 'Arapahoe' in counties: 
    print('True')
else:
    print('False')
# %%

counties = ['Arapahoe', 'Denver', 'Jefferson']
if 'El Paso' not in counties:
    print('True')
else:
    print('False')
# %%
counties = ['Arapahoe', 'Denver', 'Jefferson']
if 'El Paso' in counties:
    print('El Paso is in the list of counties.')
else:
    print('El Paso is not the list of counties.')
# %%

# Logic Operators

if 'Arapahoe' in counties or 'El Paso' in counties:
    print('Arapahoe and El Paso are in the list of counties')
else:
    print('Arapahoe or El Paso is not in the list of counties.')
# %%

if 'Arapahoe' in counties and 'El Paso' not in counties:
    print('Only Arapahoe is in the list of counties.')
else:
    print('Arapahoe is in the list of counties and El Paso is not in the list of counties.')
# %%

# Repetition Statements
# While Loop
x = 0
while x <= 10:
    print(x)
    x = x + 1
# %%
count = 7
while count < 1:
    print('Hello World')
# %%

# For Loops
for county in counties:
    print(county)
# %%
numbers = [0, 1, 2, 3, 4, 5]
for num in numbers:
    print(num)
# %%
for num in range(6):
    print(num)
# %%
for i in range(len(counties)):
    print(counties[i])
# %%

for county in counties_tuple:
    print(county)
# %%
for county in len(counties_tuple):
    print(county)
# %%
for i in range(len(counties_tuple)):
    print(counties_tuple[i])
# %%

# Iterate Through a Dictionary

counties_dict = {'Arapahoe' : 422829, 'Denver' : 463353, 'Jefferson' : 432438}

# %%
for county in counties_dict:
    print(county)
# %%
for county in counties_dict.keys():
    print(county)
# %%

# Get the Value of a Dictionary or getting a value of Keys

for voters in counties_dict.value():
    print(voters)
# %%
for county in counties_dict:
    print(counties_dict[county])
# %%
for county in counties_dict:
    print(counties_dict.get(county))
    

# %%
# Get the key-Value Pairs of a Dictionary(Key with its own value)

for key, value in dictionary_name.items():
    print(key, value)


# %%
# Get the key-Value Pairs of a Dictionary(Key with its own value)
for county, voters in counties_dict.items():
    print(county, voters)
# %%

for county, voters in counties_dict.items():
    print(county"county has", voters"registered voters.")
# %%
# Iterate Through a List of Dictionaries
# Get Each Dictionary in a List of Dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)
# %%

for i in range(len(voting_data)):
    print(voting_data[i])
# %%

# Get the Values from a List of Dictionaries
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

# %%

# How would you retrieve the number of registered voters from each dictionary
for county_dict in voting_data:
    print(county_dict['registered_voters'])
# %%
# If we only want to print the county name from each dictionary, we can use county_dict['county'] in the print statement for the for loop.

for county_dict in voting_data:
    print(county_dict['county'])
# %%
# The print() Function
#A string with integer values converted to a string using concatenation with the "+" sign. For example: 
#print("Your interest for the year is $" + str(interest)) .

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")
# %%

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")
# %%
# Using F-Strings with Dictionaries

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

# %%

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")
# %%
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")
# %%

# Multiline F-Strings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

# %%
#format the percentage of votes to two decimal places
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
# %%

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
message_to_candidate
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")


# %%
voting_data = [``{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, 
{"county":"Jefferson", "registered_voters": 432438}]
message_to_candidate
for county, voters in voting_data.items():
    print(f"{county} county has {voters} registered voters.")
# %%
