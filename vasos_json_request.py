import requests
import json
import urllib2
from urllib2 import urlopen

#data = json.load(urllib2.urlopen('http://vasos2.wrayesian.com/sites.json')) #Everything

data = 'http://vasos2.wrayesian.com/sites.json'

r = requests.get(data)

response_dict = r.json()

print(response_dict[0])

#print('\nKeys: ', len(response_dict))

repo_dict = response_dict[0]

### attempts to get rid of unicode output ('u')
### Though, it may or may not be returned by Alexa
#repo_dict = str(repo_dict)
#object_hook = response_dict[0]
#ignore_dicts = True


print("\nSelected information about the first site:")
print('USGS Location: ', repo_dict['usgs_huc_8']) 

#repo_dicts = response_dict[]

#print("Multi Metric Score Count: ", len(repo_dicts))
##repo_dict = repo_dicts[0]
##print("\nKeys:", len(repo_dict))
##
##for key in sorted(repo_dict.keys()):
##    print(key)
