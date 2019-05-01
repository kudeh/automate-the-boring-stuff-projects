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
        sendFrom(str): senders email address
        password(str): senders password
        sendTo (str): receipient email address
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

        time.sleep(10)

        composeBtnElem = browser.find_element_by_link_text('Compose')
        composeBtnElem.send_keys(Keys.ENTER)

        time.sleep(10)

        messageToElem = browser.find_element_by_id('message-to-field')
        messageToElem.send_keys(sendTo)

        messageSubjectElem = browser.find_element_by_css_selector('input[placeholder = "Subject"]')
        messageSubjectElem.send_keys('FYI')

        messageBodyElem = browser.find_element_by_css_selector('div[data-test-id = "rte"]')
        messageBodyElem.send_keys(message)

        composeSendBtnElem = browser.find_element_by_css_selector('button[data-test-id = "compose-send-button"]')
        composeSendBtnElem.send_keys(Keys.ENTER)


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
