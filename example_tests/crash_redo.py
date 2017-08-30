"""
Requesting Data Using an API Call
"""

"""
https://api.github.com/search/repositories?q=language:python&sort=stars
"""

### Processing an API Response
    # A program to issue an API call and process the results by identifying
    # the most starred Python projects on GitHub:
import requests

# Make an API call and store the response.
    # store the URL of the API call.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    # Use requests to make the call.
    # call get() and pass it the URL.
    # store the reponse object in the variable r.
r = requests.get(url)
    # print the value of status_code to make sure of a successful call.
print("Status code: ", r.status_code)

# store API response in a variable.
    # The API returns the ino in JSON format, so we use the json() method
    # to convert the information to a Python dictionary.
    # store the resulting dictionary in response_dict.
response_dict = r.json()

# Process the results.
print(response_dict.keys())


### Working with the Response Dictionary
# Now that we have our info stored as a dictionary we can work with
# the data sotred there.
# Generate some output that summarizes the info.

print("Total repositories:", response_dict['total_count'])

# Explore info about the repos
