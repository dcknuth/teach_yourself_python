import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.status_code == requests.codes.ok
len(res.text)
print(res.text[:250])
# Look, it's Romeo and Juliet
# A list of status codes can be found at:
#  https://en.wikipedia.org/wiki/List_of_HTTP_status_codes

# Look at an error
res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
res.raise_for_status()
# Gets us the HTTP code 404 for not finding a page
# We can use raise if we want the program to stop OR we could use
#  a try:/except: block if we want to try to recover and keep going

# Most things we could probably save in a single shot, but if we wanted
#  to save something large piece-by-piece we could...
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
with open('RomeoAndJuliet.txt', 'wb') as playFile:
    for chunk in res.iter_content(100000):
        playFile.write(chunk)
# This will write off to a file in pieces 100,000 bytes long until complete
#  and then close the file. 'wb' writes binary in case it's Unicode
# Probably only needed if large and we get an error writing the whole thing

# Use beautiful soup to grab a part of a web page
import bs4
res = requests.get('https://automatetheboringstuff.com/2e/chapter12/')
len(res.text)
ch12Soup = bs4.BeautifulSoup(res.text, 'html.parser')
type(ch12Soup)
# Let's try to get the chapter title
# We can inspect and see it is in <main> and <h2>
elems = ch12Soup.select('h2')
print(elems)
# Well, it's the only item in the list, but with a bunch of stuff
print(elems[0].getText())
# Ah, let try...
chapterName = elems[0].getText()[2:]
# We got it


# Try Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
