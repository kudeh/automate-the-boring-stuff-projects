#! python3
# yahoomail-emailer.py
# Author: Kene Udeh
# Source: Automate the Boring stuff with python Ch. 11 Project

import sys
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def emailer(sendFrom, password, sendTo, message):
    """ Sends message to email address
    Args:
        sendTo (str): string representing email address
        message (str): message to send
    Returns:
        None
    """
    emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+      # username
        @                      # @ symbol
        [a-zA-Z0-9.-]+         # domain name
        (\.[a-zA-Z]{2,4})      # dot-something
        )''', re.VERBOSE)

    if not emailRegex.match(sendTo):
        print("**Invalid Email Address Provided**")

    else:

        # set up selenium browser
        browser = webdriver.Firefox(executable_path='/Users/keneudeh/Downloads/geckodriver')
        browser.get('https://login.yahoo.com')

        loginUsernameElem = browser.find_element_by_id('login-username')
        loginUsernameElem.send_keys(sendFrom)
        loginUsernameElem.send_keys(Keys.TAB)
        
        nextBtnElem = browser.find_element_by_id('login-signin')
        nextBtnElem.send_keys(Keys.ENTER)

        time.sleep(10)
        
        loginPwdElem = browser.find_element_by_id('login-passwd')
        loginPwdElem.send_keys(password)
        loginPwdElem.send_keys(Keys.TAB)

        signInBtnElem = browser.find_element_by_id('login-signin')
        signInBtnElem.send_keys(Keys.ENTER)

        time.sleep(10)

        mailLinkElem = browser.find_element_by_id('uh-mail-link')
        mailLinkElem.send_keys(Keys.ENTER)

        print(sendTo, '\n', message)

        


if __name__ == '__main__':

    if len(sys.argv) > 2:
        sendTo = sys.argv[1]
        message = ' '.join(sys.argv[2:])

        sendFrom = input('Enter your yahoomail email: ')
        password = input('Enter your yahoomail password: ')

        emailer(sendFrom, password, sendTo, message)

    elif len(sys.argv) == 2:
        print('missing message to send')

    else:
        print("Add command line args %s and %s" % ("'email_address'", "'message'"))
