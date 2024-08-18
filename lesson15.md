# Python Lesson 15
Web Scraping

Web scraping is a fast moving target as web sites constantly change. We will cover some basics in the first part of the lesson and then try to do a couple examples of things that might actually help or be interesting in the second part. To start, even though we have already used the requests module a little, let’s get reacquainted with it.
```
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
```
We are going to need to look at a little HTML to see what to look for as we head to our next section. In a browser (will assume Chrome) open [Automate the Boring Stuff with Python chapter 12](https://automatetheboringstuff.com/2e/chapter12/) that this chapter is based on. Then press F12 or otherwise get into the developer tools for the browser. We will discuss some of the elements and if you are reading along, expand some sections with the arrows on the left (and some …s) and look at the <> marks. These are the pieces we can note to get the parts we want out of a web page. Let’s use the same chapter 12 link above and use the BeautifulSoup module to find something in it.
```
import bs4
res = requests.get('https://automatetheboringstuff.com/2e/chapter12/')
len(res.text)
ch12Soup = bs4.BeautifulSoup(res.text, 'html.parser')
type(ch12Soup)
# Let's try to get the chapter title
# We can inspect and see it is in <main> and <h2>
elems = ch12Soup.select('h2')
print(elems)
# Well, it's in the only item in the list, but with a bunch of stuff
print(elems[0].getText())
# Ah, let try...
chapterName = elems[0].getText()[2:]
# We got it
```
Since the on-line book only has one \<h2\> element and it is the title each time, we would just need to get the text and capture starting after the digits to get the title off of all the chapters in the on-line book. Rather than try to go through all the options in bs4, let’s just jump to a more interesting example. This time we will download some comics from [xkcd](https://xkcd.com/). Head over with your browser and open the developer tools. We are going to use a new file called downloadXkcd.py with the following
```
import requests, os, bs4

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
numComics = 10

for x in range(numComics):
    # Download the page
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    
    # Find and save the comic
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
    with open(os.path.join('xkcd', os.path.basename(comicUrl)),
                     'wb') as curImage:
        for chunk in res.iter_content(100000):
            curImage.write(chunk)
    
    # Get the Prev link
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')
    # We could also download all by stopping at previous link '#'

print("Done")
```
The only things we are changing from ATBSWP is that we only download 10 images and we put the ‘open’ inside a ‘with’. The soup.select is getting a named div and then an img element. If that succeeds, we get the src part of that. Then after a download and save, we get the previous comic’s url.

Next we want to try using Selenium, but to do so, we need to install it as it does not come with Anaconda by default. So, quit Spyder. Then run the Anaconda prompt, which should read ‘(base)’ as we are going to install in the main Conda environment. Run this
```
conda install -c conda-forge selenium
```
It should proceed to install the latest matching Selenium release after asking you if you want to proceed. Then it is likely that you have to download the driver you need from the [Selenium page](https://www.selenium.dev/documentation/webdriver/troubleshooting/errors/driver_location/#download-the-driver) or for Chrome [here](https://googlechromelabs.github.io/chrome-for-testing/). Then let’s look at our path with 'echo %PATH%' and put the downloaded driver in an existing anaconda path. This was needed for Windows, but other OSs should be similar if things don’t install automatically. The following should now work
```
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
```
Now we can go somewhere and click on stuff
```
# Go to a page
browser.get('https://inventwithpython.com')
# Click on the page
linkElem = browser.find_element('link text', 'Read Online for Free')
# Or more readable
# linkElem = browser.find_element(By.LINK_TEXT, 'Read Online for Free')
linkElem.click()
```
Let’s do it again, but a little cleaner with a wait
```
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
```
Now let’s log into something. We are going to try loggin in to WordPress, where this content was created
```
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
```
Now that we can log into an advanced page with Javascript, we should be able to access any page that does not have a captcha or other active resistance.