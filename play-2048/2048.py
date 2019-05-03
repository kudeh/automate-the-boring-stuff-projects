#! python3
# 2048.py
# Author: Kene Udeh
# Source: Automate the Boring stuff with python Ch. 11 Project

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

def play():
    """
    Args:
        None
    Returns:
        None
    """
    driver = webdriver.Firefox(executable_path='/Users/keneudeh/Downloads/geckodriver')
    driver.get('https://play2048.co/')

    key_select = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]

    gameStatusElem = driver.find_element_by_css_selector('.game-container p')
    htmlElem = driver.find_element_by_css_selector('html')
    

    while gameStatusElem.text != 'Game over!':
        
        htmlElem.send_keys(key_select[random.randint(0, 3)])
        gameStatusElem = driver.find_element_by_css_selector('.game-container p')

    score = driver.find_element_by_css_selector('.score-container').text

    print(f'You scored: {score}')



if __name__ == '__main__':
    play()