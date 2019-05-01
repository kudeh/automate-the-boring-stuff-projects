#! python3
# yahoomail-emailer.py
# Author: Kene Udeh
# Source: Automate the Boring stuff with python Ch. 11 Project

import sys
import re
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

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

        delay = 10 # seconds

        # Set up selenium browser
        browser = webdriver.Firefox(executable_path='/Users/keneudeh/Downloads/geckodriver')
        browser.get('https://login.yahoo.com')

        # Enter yahoo email address
        loginUsernameElem = browser.find_element_by_id('login-username')
        loginUsernameElem.send_keys(sendFrom)
        loginUsernameElem.send_keys(Keys.TAB)
        
        # Press 'Next' to go to password filed page
        nextBtnElem = browser.find_element_by_id('login-signin')
        nextBtnElem.send_keys(Keys.ENTER)

        # Wait for 'password' field page to load then enter password, tab to submit btn
        loginPwdElem = wait_for_page_load(browser, By.ID, 'login-passwd', delay)
        loginPwdElem.send_keys(password)
        loginPwdElem.send_keys(Keys.TAB)

        # Select 'sign in' btn, press ENTER
        signInBtnElem = browser.find_element_by_id('login-signin')
        signInBtnElem.send_keys(Keys.ENTER)

        # Click on link to redirect to mail.yahoo.com
        mailLinkElem = wait_for_page_load(browser, By.ID, 'uh-mail-link', delay)
        mailLinkElem.send_keys(Keys.ENTER)

        # Click on 'Compose' button link
        composeBtnElem = wait_for_page_load(browser, By.LINK_TEXT, 'Compose', delay)
        composeBtnElem.send_keys(Keys.ENTER)
        
        # use 'time.sleep' to wait instead of 'wait_for..', cause of refreshing issue
        time.sleep(delay)
        # Enter email address
        messageToElem = browser.find_element_by_id('message-to-field')
        messageToElem.send_keys(sendTo)
        # Enter Subject
        messageSubjectElem = browser.find_element_by_css_selector('input[placeholder = "Subject"]')
        messageSubjectElem.send_keys('FYI')
        # Enter email body
        messageBodyElem = browser.find_element_by_css_selector('div[data-test-id = "rte"]')
        messageBodyElem.send_keys(message)
        # Send email
        composeSendBtnElem = browser.find_element_by_css_selector('button[data-test-id = "compose-send-button"]')
        composeSendBtnElem.send_keys(Keys.ENTER)

def wait_for_page_load(browser, by, selector, delay):
    """ waits for page to load
    Args:
        browser (webdriver): Selenium web driver
        by (By): Selenium By object
        selector (str): selector of element, which will be available on page load
        delay (int): number of seconds to wait
    Returns:
        elem (Element): Selenium element
    """
    try:
        elem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((by, selector)))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")

    return elem

if __name__ == '__main__':

    #$ python yahoomail-emailer.py sendingto@gmail.com message I am sending

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
