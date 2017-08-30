"""
Use API to find sites for stream

"Show my all site names with corresponding id's"

"""

import json
import requests
import urllib
import urllib2


# Test simple dictionary access, starting with looping through whole
# dictionary with condition statments

# Then, test using json.loads()


url = 'https://wva-dev.sosdata.org/streams.json'

# get streams json
r = requests.get(url)

streams = r.json()

# Returns sorted (by name) and flattened
#for id, name in sorted([(d['id'],d['name']) for d in streams], key=lambda t:t[1]):
#    print'{}: {}'.format(id,name)
        
# save for possible if statement
l_comprehension = [d for d in streams if d['name'] == 'Buck Mountain Creek']
print(l_comprehension)

# Works! Prints out every stream name
#for d in streams:
#    print d['name']

# Prints every ID and every name
#for d in streams:
#    for key in d:
#        print d[key]
