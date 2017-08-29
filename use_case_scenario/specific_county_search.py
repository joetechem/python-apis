import operator, functools
import requests
import json

"""
API to get specific data from wva-dev.sosdata.org

County, Albemarle.

"""

# call to county:albemarle:sites data
sites_url = 'https://wva-dev.sosdata.org/sites.json?association=sites&parent_scaffold=counties&county_id=2'
r3 = requests.get(sites_url)

# test if call successful
if r3.status_code == 200:
    print("\tStatus code: 200, API call successful")
else:
    print("\tAPI call failed")

sites_list = r3.json()

print("\nTotal number of logged sites in Albemarle: " + str(len(sites_list)))


# call to county:albemarle:streams data
streams_url = 'https://wva-dev.sosdata.org/streams.json?association=streams&parent_scaffold=counties&county_id=2'
r2 = requests.get(streams_url)

# test if call successful
if r2.status_code == 200:
    print("\tStatus code: 200, API call successful")
else:
    print("API call failed")
    
streams_list = r2.json()

print("\nTotal number of streams in Albermarle: " + str(len(streams_list)))


# call to counties data
url = 'https://wva-dev.sosdata.org/counties.json'

    # Use requests to make the call.
    # call get() and pass it the URL.
    # store the reponse object in the variable r.
r = requests.get(url)

# test if call successful
if r.status_code == 200:
    print("\tStatus code: 200, API call successful")
else:
    print("API call failed")

# store API response in a variable.
    # The API returns the data in JSON format, so use json() method
    # to convert the data to a Python dictionary.
    # store resulting dictionary in a variable.
counties_list = r.json()

print("\nTotal number of vasos counties: " + str(len(counties_list)))
