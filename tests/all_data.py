import math
import json
import urllib2
from urllib2 import urlopen


data = json.load(urllib2.urlopen('http://vasos2.wrayesian.com/sites.json')) #Everything


#This is the list of name, score, lat, and long for each stream from the list data
all_streams_data = []
for x in range(0,len(data)-1):
	if(data[x]['latitude'] != None and data[x]['longitude'] != None):
		all_streams_data.extend([str(data[x]['usgs_huc_8'])[10:]])
		all_streams_data.extend([[data[x]['multi_metric_score'],data[x]['latitude'].split(" ",1)[0],data[x]['longitude'].split(" ",1)[0]]])
