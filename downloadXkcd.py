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
