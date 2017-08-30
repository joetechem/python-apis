"""
Looking for best way to return the data a user requests.
"""

import requests
import json

# Make an API call and store the response.
    # store the URL of the API call.
url = 'https://wva-dev.sosdata.org/counties.json'

    # Use requests to make the call.
    # call get() and pass it the URL.
    # store the reponse object in the variable r.
r = requests.get(url)

    # print the value of status_code to make sure of a successful call.
print("Status Code:", r.status_code)

# store API response in a variable.
    # The API returns the ino in JSON format, so we use the json() method
    # to convert the information to a Python dictionary.
    # store the resulting dictionary in response_dict.
counties_list = r.json()

# Test for success
print(counties_list)

### The vasos json is nested dictionaries in a list   ###
### Each county has own dictionary containing id and name ###
### nested inside the list, counties_dict. ###

# returns the first dictionary in the list
albemarle = counties_list[0]

### Simple Dictionary Access
#print("\nCounty id: " + str(albemarle['id']))
#print("County name: " + str(albemarle['name']))


""" Retrieve County name and ID for county """
print("\nReturned County name and id:")
print("\tCounty id: " + str(albemarle['id']))
print("\tCounty name: " + str(albemarle['name']))


""" Retreieve streams for county """

streams_url = 'https://wva-dev.sosdata.org/streams.json'
r2 = requests.get(streams_url)
print("Status Code:", r2.status_code)
streams_list = r2.json()
print(streams_list)

# Simple test to find stream in Albemarle county
for stream in streams_list:
    if stream["name"] == "Buck Mountain Creek":
        print("yes")
        


for streams in streams_list[0:41]:
    # returning all streams
    # print(streams)
    [d['Meadow Creek'] for d in streams_list if 'Meadow Creek' in d]

#for key, value in streams_dict.items():
#    print("\nKey: " + key)
#    print("Value: " + value)

















