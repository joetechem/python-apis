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

url = 'https://wva-dev.sosdata.org/counties.json'

r = requests.get(url)
