import requests
import pandas as pd

#   This time, I'm thinking I should develop a measure of how much different papers are covering crime.
# do newspapers in cities with more crime cover it more?   Or, rather, which newspapers take notice when
# there is a crime wave going on in their city?
#   There are limitations to using this "search" method.  Perhaps we should be checking for articles that have
# "yesterday", "this week", "this morning" or something to that effect in their text.  That way, we know they
# are discussing recent crime rather than a crime long ago.
#   Another limitation is that cities with higher crime may be more prone to writing summary articles.  When Chicago
# has 50 shootings in a weekend, even very crime-centric paper could be inclined to write a summary article of all of
# the shootings, and then perhaps cover only a few of the victims.  We can probably handle that by taking the square
# root of crime in the city.
#   I suppose this also means that we're going to focus in on a couple of major cities.  Perhaps just look at NYC,
# LA, and Seattle.  Then, 

cities = [  'Atlanta',
            '/"District of Columbia/"',
            'Seattle',
            'St. Louis',
            'New York',
            'Madison',
            'Chicago',
            'Los Angeles',
            'San Francisco',
            'Miami',
            'Orlando',
            'Columbus',
            'Boston',
            'Portland',
            'Detroit',
            'Baltimore',
            'Pittsburgh',
            'Oakland',
            'Houston',
            'Philadelphia',
            'Newark',
            'Dallas',
            'Austin',
            'Cleveland',
            'Denver',
            'Tampa',
            'Sacramento',
            'Kansas City',
            'Las Vegas',
            'Phoenix',
            'Salt Lake City',
            'San Diego',
            'Cincinnati',
            'Indianapolis',
            'Oklahoma City',
            'San Antonio'
            ]
queries = ['any','violence','looting','arson']

df = pd.DataFrame({     'city' : sorted(cities * len(queries)),
                        'query': queries * len(cities),
                        'hits' : [0] * len(queries) * len(cities) })

subscription_key = "29e9c06b82784655862dca3cf8fe773d"
endpoint  = 'https://api.cognitive.microsoft.com/bing/v7.0/news/search'
since       = '2020-06-30'
headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
params  = { "q": search_term,
            "sortBy": "Date",
            "since": since,
            "textDecorations": True,
            "textFormat": "HTML"
            }

for i, city, query in zip(df.index, df['city'], df['query'] ):
    print(i)
    print(city)
    print(query)
    if query == "any":
        params['q'] = city
    else:
        params['q'] = city + '+' + query
    df.iloc[i,2] = requests.get(endpoint, params = params, headers = headers).json()['totalEstimatedMatches']

df.to_csv('unrest.csv')