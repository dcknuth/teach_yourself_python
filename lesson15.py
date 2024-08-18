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
# Go to a page
browser.get('https://inventwithpython.com')
# Click on the page
linkElem = browser.find_element('link text', 'Read Online for Free')
# Or more readable
# linkElem = browser.find_element(By.LINK_TEXT, 'Read Online for Free')
linkElem.click()

# Close the web browser and do it again, but make sure the page is
#  loaded with a wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome()
browser.get('https://inventwithpython.com')
# Wait for an element to be visible on the page
element = WebDriverWait(browser, 10).until(
    EC.visibility_of_element_located((By.LINK_TEXT,
                                      'Read Online for Free')))
element.click()
# Close the browser after we see it worked
browser.quit()

# What if we need to log into the website we are targeting
from getpass import getpass
password = getpass("Enter your password: ")
# Yes, this fails to hide in IPython, but would work if in a script
#  run from the command line. It would also show in our Variable
#  Explorer, so test with a non-real password
# Test pw is NotTheActualPassword
username = 'test_wp'
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 30)
browser.get('https://davidknuth.com/blog/wp-login.php')
wait.until(EC.element_to_be_clickable((By.ID, 'user_login')))\
    .send_keys(username)
wait.until(EC.element_to_be_clickable((By.ID, 'user_pass')))\
    .send_keys(password)
wait.until(EC.element_to_be_clickable((By.ID, 'wp-submit')))\
    .click()
print("Logged in")
browser.quit()
