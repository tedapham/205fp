### need package reverse_geocoder

import pandas as pd
import numpy as np 
import reverse_geocoder as rg

## name of file
df = pd.read_csv('quake_data.csv')
def StateAbbrev(state):
	us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
	}
	try:
		return us_state_abbrev[state]
	except:
		return None

# Get coordinates from the dataframe

lonlat = df[['lat','lon']]
coordinates = [tuple(x) for x in lonlat.values]

# get states 
## use reverse_geocoder
geo_reverse = rg.search(coordinates)
states = [StateAbbrev(geo_reverse[i]['admin1']) for i in range(len(geo_reverse))]
counties = [geo_reverse[i]['admin2'] for i in range(len(geo_reverse))]

df['state'] = states
df['county'] = counties

df.to_csv('quake_data_clean.csv')

