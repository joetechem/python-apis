"""

"Show me all streams for this county"

"""

import json
import requests

# Albemarle County
url = 'https://wva-dev.sosdata.org/streams.json?association=streams&parent_scaffold=counties&county_id=2'

r = requests.get(url)

streams = r.json()

print("\nShowing sorted list of streams and their corresponding id's in alphabetical order" + "\n")
for id, name in sorted([(d['id'],d['name']) for d in streams], key=lambda t:t[1]):
    print'{}: {}'.format(id,name)


