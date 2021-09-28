import bs4
import requests
import time
import telegram_send

while True:
    getPage = requests.get('https://www.ebuyer.com/store/Components/cat/Graphics-Cards-Nvidia?outlet=1&q=')
    getPage.raise_for_status()
    soup = bs4.BeautifulSoup(getPage.text, 'html.parser')
    number1 = soup.select('.taxonomy-title__count')
    time.sleep(25)
    getPage = requests.get('https://www.ebuyer.com/store/Components/cat/Graphics-Cards-Nvidia?outlet=1&q=')
    getPage.raise_for_status()
    soup = bs4.BeautifulSoup(getPage.text, 'html.parser')
    number2 = soup.select('.taxonomy-title__count')
    if number2 != number1:
        telegram_send.send(messages=["Stock Changed!\n" + str(number2) + "\nhttps://www.ebuyer.com/store/Components/cat/Graphics-Cards-Nvidia?outlet=1&q="])
    else:
            print(number2)






