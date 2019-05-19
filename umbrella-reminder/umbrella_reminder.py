#! python3
# umbrella_reminder.py
# Author: Kene Udeh
# Source: Automate the Boring stuff with python Ch. 16 Project

import requests
import bs4
from twilio.rest import Client


def rain_check():
    """Checks if it's going to rain
    Args:
        None
    Returns:
        rain (bool): True if rainy
    """
    url = 'https://weather.com/en-CA/weather/today/l/CAON4756:1:CA'
    rain = False

    try:
        res = requests.get(url)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        weather_elem = soup.select('.today_nowcard-phrase')

        if 'rain' in weather_elem[0].text.lower():
            rain = True

    except Exception as exc:
        print(exc)

    return rain


def send_reminder(accountSID, authToken, myTwilioNumber, myCellPhone):
    """Sends a text using twilio
    Args:
        accountSID (str): twilio acct sid
        authToken (str): twilio authentication token
        myTwilioNumber (str): twilio number
        myCellPhone (str): my cell phone number
    Returns:
        None
    """
    twilioCli = Client(accountSID, authToken)
    message = twilioCli.messages.\
    create(body='Rain Alert! Water is (not) wet. Grab an Umbrella bro.',\
           from_=myTwilioNumber, to=myCellPhone)



if __name__ == "__main__":

    if rain_check():
        send_reminder('A***************', 'A**************', '+1********', '+1**********')