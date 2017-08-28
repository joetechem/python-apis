"""
Local Python Client Testing

Objective: create a python client (or node.js) to take a county or stream
            as input and use API to get the site.
            The logic needs to use counties or stream to find the county
            or stream id, then use something like this...
            https://wva-dev.sosdata.org/sites.json?association=sites&parent_scaffold=streams&stream_id=197
            to look up the sites.

"""


# depends
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
print(counties_list)

### The vasos json is nested dictionaries in a list   ###
### Each county has own dictionary containing id and name ###
### nested inside the list, counties_dict. ###

"""
Creating Small Test Case
    Logic:
    User asks for County I.D. and # of Sites within that county
    County to be tested = Albemarle

    Process:
    Create a function to..
    - *Assign each item (dictionary for every county) in the list a variable name?
    - specify index position of called county,
    - print called county id --> [0] and name --> .....*come back to this


    Thoughts: would one need to create a variable for each dictionary(county)?

    
"""
# returns total number of counties
print("\nTotal number of counties: " + str(len(counties_list)))

# returns the first dictionary in the list
albemarle = counties_list[0]
print("\nFirst County: ", albemarle)










#county_dict_item = counties_list[0]
#print(county_dict_item)

# Process results.
#print(response_dict.keys())




