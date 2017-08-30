# coding: utf-8

import ui
import shelve
import location
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

# Setting up variables for the views (in lieu of using the NavigationView)
item_db = None
add_item = None
show_item = None
search_items = None
search_results = None
search_county = None
num = 0
num2 = 0


vacounties = json.load(urllib2.urlopen('http://vasos2.wrayesian.com/counties.json'))

# Initializing the database and view
# shelve is essentially just like a Python dictionary, only the dictionary is saved
# to the filesystem so that the data persists. It will be interesting to see how or
# even if this translates when converting for a native iOS app in XCode.
_db = shelve.open('test1') # the string is the filename used for the database	
names = _db.keys() # This simply gets the list of keys in the dictionary
db = ui.ListDataSource(names) # This data source is used by the main screen list

# Syncing the database and view -- to be called every time an item is saved
#
def sync_db():
	_db.sync()
	names = _db.keys()
	db.items = names # resetting the items in the data source should cause a refresh of the list
	print('resetting: ' + str(names))


############################## Models ##############################

# Item class -- specific to database structure
# This will help persist and retrieve items from an ordered tuple in a dictionary keyed by name.
class Item (object):
	
	# Attributes are listed here
	# Simply add more if you want more
	# Please note that the "name" attributes is used as the key in the
	# shelf dictionary (primary key)
	# Also, note the dictionary works like this:
	# d = { name: (name, type, rating, ...)}
	# It is keyed by name with a tuple containing all attributes (repeating name)
	# So, to add attributes, just add them to the model and the tuple used to save.
	name = ''
	type = ''
	rating = 0
	ph = ''
	
	def _load_from_tup(self,name):
			self.name = name
			tup = _db[self.name]
			self.type = tup[1]
			self.rating = tup[2]
			self.ph = tup[3]
	
	# Coupled to dictionary structure
	# type is required for new item
	#
	def __init__(self, name=None, type=None, rating=None, ph=None):
		self.name = name
		if self.name is None:
			pass	
		elif type is None:
			self._load_from_tup(name)
		else:
			self.type = type
			self.rating = rating
			self.ph = ph
				
	# Coupled to dictionary structure
	#
	def save(self):
		# Making sure name is not an empty string
		if len(self.name) != 0:
			_db[self.name] = (self.name,self.type,self.rating,self.ph)
			sync_db()		
	
	# Coupled to dictionary structure
	#
	@staticmethod
	def find(key):
		print("looking up " + key)
		item = Item()
		item._load_from_tup(key)
		return item
		
	# Coupled to dictionary structure and not that efficient since this is essentially
	# a no-sql db :)
	#
	@staticmethod
	def find_by_type(type):
		results = []
		for key in _db.keys():
			if _db[key][1] == type:
				results.append(key)
		return results
#################################################################


######### View Callbacks, Delegates, and helpers #################

# Callback used when adding a new item
#
def add_item(sender):
	print("Clicked add button: " + add_item['item_name'].text)
	name = str(add_item['item_name'].text)
	type = add_item['item_type'].data_source.items[add_item['item_type'].selected_row[1]]
	print(add_item['item_type'].data_source.items)
	print(type)
	rating = int(add_item['item_rating'].value * 10)
	ph = add_item['item_ph'].data_source.items[add_item['item_ph'].selected_row[1]]
	
	item = Item(name,type,rating,ph)
	item.save()
	add_item.close()
	add_item.send_to_back()
	item_db.bring_to_front()
	

# Callback used to present the add new item sheet
def add(sender):
	print("Clicked on plus")
	item_db.send_to_back()
	add_item.present('sheet')
			

# Callback used to present the search items sheet
def search(sender):
	print("Clicked on search")
	item_db.send_to_back()
	search_item.present('sheet')
	
def countysearch(sender):
	print("Clicked on search by county")
	item_db.send_to_back()
	search_county.present('sheet')
	

county_sites = []

def go_search(sender):
	print("Clicked on GO SEARCH")
	item_db.send_to_back()
	gosearchitem = str(sender.superview['county_search'].text)
	for x in range(0,len(vacounties)-1):
		if(vacounties[x]['name'] == gosearchitem):
			print("Found " + gosearchitem)
			num = x
			print num
	try: num
	except NameError: num = None
	if(num is None):
		healthtv = search_county['healthtv']
		healthtv.data_source.items = ["Try again please!"]
	else:
		print(vacounties[num]['name'] + " " + str(vacounties[num]['id']))
		county_sites = json.load(urllib2.urlopen('http://vasos2.wrayesian.com/streams.json?association=streams&county_id=' + str(vacounties[num]['id']) + '&parent_scaffold=streams&parent_scaffold=counties'))
		print county_sites
		sites = []
		for x in range(0,len(county_sites)):
			if county_sites[x]['name'] not in sites:
				sites.extend([county_sites[x]['name']])
		print sites
		go_search_list = search_county['gosearchtv']
		go_search_list.data_source.items = sites
		go_search_list.allows_selection = True

def gethealth(sender):
	print("Chose a stream")
	req_site = search_county['gosearchtv'].data_source.items[search_county['gosearchtv'].selected_row[1]]
	print req_site + "<-- clicked on"
	for x in range(0,len(all_streams_data)/2):
		print("..." + all_streams_data[2*x])
		if(all_streams_data[2*x] == req_site):
			print("Found " + req_site)
			num = 2*x
			print num
	try: num
	except NameError: num = None
	if(num is None):
		health_val = "None"	
	else:	
		health_val = all_streams_data[num+1][0]
	healthtv = search_county['healthtv']
	print health_val
	healthtv.data_source.items = ["Health: " + str(health_val)]

nearby_list = []
rad = 5
location.start_updates()
loc = location.get_location()
location.stop_updates()
loc_long = loc['longitude']
loc_lat = loc['latitude']
def findnearby(sender):
	print("Clicked on Nearby")
	item_db.send_to_back()
	nearby_view.present('sheet')
	
	print("Got location")
	
def getnearbyhealth(sender):
	print("Chose a stream")
	health = nearby_view['nearbytv'].data_source.items[nearby_view['nearbytv'].selected_row[1]]
	print health
	for x in range(0,len(all_streams_data)):
		if(all_streams_data[x] == health):
			print("Found " + health)
			num = x
			print num
		
	health_val = all_streams_data[num+1][0]
	healthtv = nearby_view['healthtv']
	healthtv.data_source.items = ["Health: " + str(health_val)]
	if(int(health_val) < 5):
		nearby_view.background_color = '#ffaaaa'
	elif(int(health_val) < 9):
		nearby_view.background_color = '#ffffaa'
	elif(int(health_val) > 8):
		nearby_view.background_color = '#aaffaa'
	else:
		nearby_view.background_color = (0.0,0.0,0.0,0.0)
	
def update(sender):
	nearby_list = []
	far_list = []
	rad = int(nearby_view['nearbyslider'].value * 5)
	print("Got radius: " + str(rad))
	for x in range(0,len(all_streams_data)/2):
		print(x)
		if(math.sqrt((float(all_streams_data[2*x-1][1])-float(loc_lat))**2+(float(all_streams_data[2*x-1][2])-float(loc_long))**2) <= rad):
			nearby_list.extend([all_streams_data[2*x]])
		else:
			far_list.extend([all_streams_data[2*x]])
	
	nearbytv_list = nearby_view['nearbytv']
	nearbytv_list.data_source.items = nearby_list
	nearbytv_list.allows_selection = True
	nearby_count = nearby_view['count']
	nearby_count.data_source.items = [str(len(nearby_list))]
	print "======================" + str(len(nearby_list))
	print nearby_list
	print "======================" + str(len(far_list))
	print far_list
	
	
# Search Table View Delegate	
class TypeFilterListDelegate (object):
	def _populate_results(self, results):
		results_item_list.data_source.items = results
				
	def tableview_did_select(self, tableview, section, row):
		type = tableview.data_source.items[row]
		print("Selected: " + str(type))
		results = Item.find_by_type(type)
		self._populate_results(results)
		item_db.send_to_back()
		search_results.present('sheet')
	
# Main Table View Delegate
class MainItemListDelegate (object):
	def _populate_show(self, item):
		show_item['item_name'].enabled = False
		show_item['item_name'].text = item.name
		show_item['item_type'].enabled = False
		show_item['item_type'].text = str(item.type)
		show_item['item_rating'].enabled = False
		show_item['item_rating'].text = str(item.rating)
		show_item['item_ph'].enabled = False
		show_item['item_ph'].text = str(item.ph)
		
	def tableview_did_select(self, tableview, section, row):
		print("Selected: " + str(row))
		item = Item.find(tableview.data_source.items[row])
		self._populate_show(item)
		item_db.send_to_back()
		show_item.present('sheet')
		
		
def get_county_ids():
	for x in range(0,len(county_ids)-1):
		all_streams_data

###################################################################

# Main View
item_db = ui.load_view('ItemDB')
# Add Item View
add_item = ui.load_view('NewItem')
# Show Item View
show_item = ui.load_view('ShowItem')
# Search Items View
search_item = ui.load_view('SearchItem')
# Search Results View
search_results = ui.load_view('SearchResults')

search_county = ui.load_view('SearchCounty')

nearby_view = ui.load_view('Nearby')



# Setup the db and item lists initially
main_item_list = item_db['item_list']
main_item_list.data_source = db
main_item_list.delegate = MainItemListDelegate()
main_item_list.allows_selection = True

search_item_list = search_item['item_type']
search_item_list.delegate = TypeFilterListDelegate()
search_item_list.allows_selection = True

results_item_list = search_results['results']
# Using the same delegate as the main view list because it should go to details when selected too
results_item_list.delegate = MainItemListDelegate()
results_item_list.allows_selection = True

# Present the main screen (item list)
item_db.present('sheet')

