import requests
import pandas as pd

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