"""
Use API to find sites for specific stream

"Show me all sites for this stream"

"""

import json
import requests

# Albemarle County
url = 'https://wva-dev.sosdata.org/sites.json?association=sites&parent_scaffold=counties&county_id=2'

r = requests.get(url)

streams = r.json()

