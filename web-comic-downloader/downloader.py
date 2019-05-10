#! python3
# downloader.py
# Author: Kene Udeh
# Source: Automate the Boring stuff with python Ch. 15 Project

import os
import shelve

import requests
import bs4


def download(url):
    """ Checks if comic website(buttersafe) updated, and saves comic
    Args:
        url (str): url of comic site
    Returns:
        None
    """
    # make requests to website
    try:
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; \
                   Intel Mac OS X 10_12_6) AppleWebKit/537.36 \
                   (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'}
        res = requests.get(url, headers=headers)
        res.raise_for_status()
    except Exception as exc:
        print(exc)

    # use bs4 to check contents of date
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    dateElem = soup.select('#headernav-date')
    currDate = dateElem[0].text.strip()

    # shelf file
    shelfFile = shelve.open('prevDate')
  
    if not shelfFile.keys():   # if shelve is empty, first time function runs
        print('----first ever request----')
        shelfFile['prev'] = currDate
        
    else:
        print('staring daily check...')
        prevDate = shelfFile['prev']
        
        # return from function if site hasn't been updated
        if prevDate == currDate:
            print('no updates available...')
            return

    # if update was made, get image url, make request & save
    imgUrl = soup.select('#comic > img')[0].get('src')
    os.makedirs('comics', exist_ok=True)
    try:
        print('making comic image request...')
        res2 = requests.get(imgUrl, headers=headers)
        print('saving comic image...')
        with open(os.path.join('comics', os.path.basename(imgUrl)), 'wb') as imgFile:
            for chunk in res2.iter_content(100000):
                imgFile.write(chunk)
    except Exception as exc:
        print(exc)

    # update and close shelve file
    shelfFile['prev'] = currDate
    shelfFile.close()


if __name__ == "__main__":
    download('http://www.buttersafe.com')