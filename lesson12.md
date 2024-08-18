# Python Lesson 12
CSV and JSON

This actually matches with chapter 16 of Automate the Boring Stuff with Python. We are going to put web scraping toward the end as a pretty advanced topic and this section will give you one way to work with spreadsheets, so we are skipping the spreadsheet chapters (and the PDF and Word ones). CSV stands for “comma separated values,” and CSV files are like simple spreadsheets stored as plaintext. At least, that is how most people use them. Let’s first read in an example with just file operations. Before starting, copy the following code section into a file named “example.csv”.
```
4/5/2015 13:34,Apples,73
4/5/2015 3:41,Cherries,85
4/6/2015 12:46,Pears,14
4/8/2015 8:59,Oranges,52
4/10/2015 2:07,Apples,152
4/10/2015 18:10,Bananas,23
4/10/2015 2:40,Strawberries,98
```
Now save the next one into a file named “exampleWithHeader.csv”.
```
Date,Fruit Type,Quantity
4/5/2015 13:34,Apples,73
4/5/2015 3:41,Cherries,85
4/6/2015 12:46,Pears,14
4/8/2015 8:59,Oranges,52
4/10/2015 2:07,Apples,152
4/10/2015 18:10,Bananas,23
4/10/2015 2:40,Strawberries,98
```
Now we can work with them.
```
# Since it is just a text file, we can use open
with open("example.csv") as f:
    rows = f.read().strip().split("\n")

# Then let's print the values as a table
for row in rows:
    for value in row.split(','):
        print(value.center(16), end='')
    print()
```
This works for our simple file, but what about files that have a comma in the text, or other troublesome formatting items? We can use the csv module for a little easier import of CSV files.
```
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
```
Let move to Pandas to get what is probably the best current way to read in a CSV or other data file. Let’s assume we now have a header row that gives our columns names.
```
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
```
Pandas can read many file formats in many variations and takes care of a lot of formatting that we probably want to do when we import data. We may do more with Pandas and NumPy at the end of the lesson set as they are quite useful for a number of different project types. For now, let's move on to looking at another very common, plain-text data format, JSON. JSON stands for "JavaScript Object Notation" and is often used with web API calls when you need to send or receive data even with things that have nothing to do with JavaScript. Of course, there is a module to help us with JSON.
```
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
```
We could also read or write to a file as JSON is just text. Let’s do an example of the type of thing most folks would do with JSON, get some info from a web API. To do this we will need an account with the web site we are going to fetch data from. You can do that for OpenWeatherMap by going [here](https://home.openweathermap.org/users/sign_up). We will be limited to only a few API calls a day, but that's OK. Let's try the example that was emailed with the APPID, getting the current weather in London.
```
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
```
If we had an issue, there would be some error information printing when we tried the response.raise_for_status() function. Let’s also try a slight variation. San Jose is a large city coving a lot of area and might have different weather reports for different parts. Let try asking for the weather at the exact school location after looking it up in Google Maps.
```
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
```
We could try a few other things, like getting the forecast for the next couple of days, asking for the temp to already be in Fahrenheit (imperial) or printing out the wind speed if it is given. There are many sites with APIs similar to this and most of them default to returning your data in JSON, just like we saw here.

[Python Lesson 13](lesson13.md) - Time, Scheduling and Launching Programs