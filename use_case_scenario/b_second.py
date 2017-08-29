import operator, functools
import requests
import json

"""
API to get specific data from wva-dev.sosdata.org

This tests calls for the county, Albemarle.

"""

# API call to Albemarle county data
sites_url = 'https://wva-dev.sosdata.org/sites.json?association=sites&parent_scaffold=counties&county_id=2'
r2 = requests.get(sites_url)
print("Status Code:", r2.status_code)
sites_list = r2.json()

if r2.status_code == 200:
    print("API call successful")

else:
    print("API call failed")


print("\nTotal number of sites: " + str(len(sites_list)))




streams_url = 'https://wva-dev.sosdata.org/streams.json?association=streams&parent_scaffold=counties&county_id=2'
r2 = requests.get(streams_url)
print("Status Code:", r2.status_code)
streams_list = r2.json()

if r2.status_code == 200:
    print("API call successful")

else:
    print("API call failed")


print("\nTotal number of streams: " + str(len(streams_list)))
