import operator, functools # to be used later
import requests
import json

"""
API to get specific data from wva-dev.sosdata.org

Testing a simple use-case.

Trying out different api calls: first, at top of parent (or lowest child?);
                                Second, then more sepcific calls.

User searches for how many:
    1 - Counties
    2 - Streams in a specific county ("Albemarle")
    3 - Sites in that county

"""

input_1 = raw_input("What county would you like to search the id for? ")

if input_1 == 'albemarle':

    url = 'https://wva-dev.sosdata.org/counties.json'
    r = requests.get(url)
    counties_list = r.json()


    if key in counties_list
    
    county = input_1

    print("\nReturned County name and id:")
    print("\tCounty id: " + str(county['id']))
    

# call to counties data
print("\n")
print("- " * 10)
url = 'https://wva-dev.sosdata.org/counties.json'

    # Use requests to make the call.
    # call get() and pass it the URL.
    # store the reponse object in the variable r.
r = requests.get(url)

# test if call successful
if r.status_code == 200:
    print("Status code: 200, call successful")
else:
    print("call failed, hang up and dial again")

# store API response in a variable.
    # The API returns the data in JSON format, so use json() method
    # to convert the data to a Python dictionary.
    # store resulting dictionary in a variable.
counties_list = r.json()

print("\n\tTotal number of vasos counties: " + str(len(counties_list)))


print("\n")
print("- " * 10)
# call to county:albemarle:streams data
streams_url = 'https://wva-dev.sosdata.org/streams.json?association=streams&parent_scaffold=counties&county_id=2'
r2 = requests.get(streams_url)

if r2.status_code == 200:
    print("Status code: 200, call successful")
else:
    print("call failed, hang up and dial again")
    
streams_list = r2.json()

print("\n\tTotal number of streams in Albermarle: " + str(len(streams_list)))


print("\n")
print("- " * 10)
# call to county:albemarle:sites data
sites_url = 'https://wva-dev.sosdata.org/sites.json?association=sites&parent_scaffold=counties&county_id=2'
r3 = requests.get(sites_url)

if r3.status_code == 200:
    print("Status code: 200, call successful")
else:
    print("call failed, hang up and dial again")

sites_list = r3.json()

print("\n\tTotal number of sites in Albemarle: " + str(len(sites_list)))





