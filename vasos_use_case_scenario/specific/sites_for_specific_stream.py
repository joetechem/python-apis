"""
Use API to find sites for specific stream

1 - streams in county 
1a - sites in county

    2 - sites for a stream

       3 - site data for that stream
       3a - data for one certain site

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


def all_site_data():
    print "\nShowing list of site data for streams in Albemarle county, sorted by station identifier:"
    for id, name in sorted([(d['id'],d['station_identifier']) for d in sites], key=lambda t:t[1]):
        print'{}: {}'.format(id,name)
# uncomment to show site data
#site_data()


######### 3 ######## site data for that stream
# This time testing with user input
user_says = raw_input("\nType 'y' to show site data for Buck Mountain Creek: ")
if user_says == 'y':
    def buck_site_data():
        print "\nShowing list of site data for Buck Mountain Creek, sorted by station identifier:"
        for id, name in sorted([(d['id'],d['station_identifier']) for d in buck_mtn_sites_data], key=lambda t:t[1]):
            print'{}: {}'.format(id,name)
buck_site_data()


######### 3a ######## site data for that stream
    # 8/30 currently returns same as above. taking a break.
    # Probably need to call to more nested instead of same data as in 2, above

##active = True
##while active:
##    user_says_2 = raw_input("\nType 'a' to show site data for BKM01" +
##                        ", 'b' for BKU03" +
##                        ", or 'c' for BKM1" +
##                        ", 'q' to quit: ")
##    if user_says_2 == 'a':
##        buck_mtn_creek = [d for d in sites if d['station_identifier'] == 'BKM01']
##        for id, station, metric, eco in sorted([(d['id'],d['station_identifier'],d['multi_metric_score'],d['ecological_conditions']) for d in buck_mtn_creek], key=lambda t:t[1]):
##            print'{}: {}'.format(id,station,metric,eco)
##        active = False

##    if user_says_2 == '2'
        


    
    

# py list comprehension
# Test for retrieving specific site data
#buck_mtn_creek = [d for d in sites if d['station_identifier'] == 'BKM01']

# uncomment to show BKMO1 site data
#print buck_mtn_creek


