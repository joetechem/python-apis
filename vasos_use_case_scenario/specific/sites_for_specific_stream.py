"""
Use API to find sites for specific stream

"Show me all sites for this stream"


1 - streams in county 
1a - sites in county

    2 - sites for a stream

       3 - site data for that stream 

"""

import json
import requests

######### 1 ######## streams in county
streams_url = 'https://wva-dev.sosdata.org/streams.json?association=streams&parent_scaffold=counties&county_id=2'
r2 = requests.get(streams_url)
streams_list = r2.json()
print "Pulling site data from Albemarle county..."
print("\nTotal number of streams in Albermarle: " + str(len(streams_list)))


######### 1a ######## sites in county
sites_url = 'https://wva-dev.sosdata.org/sites.json?association=sites&parent_scaffold=counties&county_id=2'
r = requests.get(sites_url)
sites = r.json()

print("\nTotal number of sites in Albemarle: " + str(len(sites)))


######### 2 ######## sites for a stream
buck_mtn_sites_url = 'https://wva-dev.sosdata.org/sites.json?association=sites&parent_scaffold=streams&stream_id=72'
r = requests.get(buck_mtn_sites_url)
buck_mtn_sites_data = r.json()

print "\nShowing list of site data for streams in Albemarle county, sorted by station identifier:"
for id, name in sorted([(d['id'],d['station_identifier']) for d in sites], key=lambda t:t[1]):
    print'{}: {}'.format(id,name)


######### 2 ######## site data for that stream 


# py list comprehension
# Test for retrieving specific site data
buck_mtn_creek = [d for d in sites if d['station_identifier'] == 'BKM01']

# uncomment to show BKMO1 site data
#print buck_mtn_creek


