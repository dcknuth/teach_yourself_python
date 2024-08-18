# Since it is just a text file, we can use open
with open("example.csv") as f:
    rows = f.read().strip().split("\n")

# Then let's print the values as a table
for row in rows:
    for value in row.split(','):
        print(value.center(16), end='')
    print()

# There is a module to help with files that are not as simple
import csv
with open("example.csv") as f:
    exampleReader = csv.reader(f)
    exampleData = list(exampleReader)
for row in exampleData:
    for value in row:
        print(value.center(16), end='')
    print()
# This has already done the row splitting for us
# It is also nice that we have row - column access
# With zero based indexing, we get the cell for Cherries with:
print(exampleData[1][1])
# If we had a very large file, we could read in the file in sections
# There is also a csv.writer() function to nicely get things back into
#  a csv file. There are also ways to deal with variations of the
#  format, but let's spend more of our time with the last way to deal
#  with a CSV file

# Try using Pandas, included with Anaconda
import pandas as pd
data = pd.read_csv('exampleWithHeader.csv')
# Looking in the Variable Explorer, we can see that we ended up with a
#  DataFrame object.
print(data)
# Not only is the DataFrame expandable from the Variable Explorer, it
#  also prints very nice by default
# Can we still address an item with a row - value?
print(data[1][1])
# Well, not in the same way as a list of lists
print(data.at[1, "Fruit Type"])
# Also interesting
print(type(data.at[1, "Quantity"]))
# It converted the quantities into numbers for us, so we don't have
#  to convert from a string to an int to be able to do things like:
print("The total number of fruits is", sum(data["Quantity"]))

# On to JSON ()
someJson = '{"name": "Zophie", "isCat": true, "miceCaught": 0' + \
    ', "napsTaken": 37.5, "felineIQ": null}'
import json
catFromJson = json.loads(someJson)
# For this case, it loads to a dictionary and does a nice job of
#  interpreting the type of each piece of data for us
# We can also go from our dictionary back to JSON
outJson = json.dumps(catFromJson)
someJson == outJson
# The types of values we can get in and out of JSON are:
#  dict, list, int, float, str, bool, or None (null in JSON)
# These can be nested to form deep and complex data exchanges

# Now try exchanging JSON data with a web site
# This will use OpenWeatherMap
# The request will need a key that you can get from the website
APPID = 'PUT_YOUR_APPID_HERE'
import requests
web_site = 'https://api.openweathermap.org/data/2.5/weather?'
loc = f'q=London,uk&APPID={APPID}'
url = web_site + loc
response = requests.get(url)
response.raise_for_status()
print(response.text)
# That looks like JSON alright, but temps are in Kelvin
weatherData = json.loads(response.text)
# Print a couple things
cityName = weatherData['name']
tempF = (weatherData['main']['temp'] - 273.15) * 9 / 5 + 32
desc = weatherData['weather'][0]['description']
print("The weather in", cityName, 'is currently ', end='')
print(f'{tempF} degrees and', desc)

# That's OK, but let's make a function to do the print and change the
#  description to deal with clouds or sun with a better temp
def print_weather(w):
    cityName = w['name']
    tempF = (w['main']['temp'] - 273.15) * 9 / 5 + 32
    desc = w['weather'][0]['description']
    if 'sunny' in desc:
        desc = 'and ' + desc
    else:
        desc = 'with ' + desc
    print("The weather in", cityName, 'is currently ', end='')
    print(f'{tempF:.1f} degrees', desc)

print_weather(weatherData)

# The following is the lattitude and longitude of Noter Dame High School
lat = 37.3282942
lon = -121.885084
url = web_site + f'lat={lat}&lon={lon}&APPID={APPID}'
response = requests.get(url)
response.raise_for_status()
print(response.text)
# Even though we used the coordinates of the school from Google maps
#  it still came up with the correct city and put it in "name". So
#  our print function should still work
weatherData = json.loads(response.text)
print_weather(weatherData)
