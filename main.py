from bs4 import BeautifulSoup
import requests
import  re

link = requests.get('https://www.olx.pl/dla-dzieci/zabawki/q-lego/?page=')
soup = BeautifulSoup(link.text, 'html.parser')
pages = int(input("How much pages do you want to webscraping: "))
number = int(1)

def checker(name):
    digital_code = re.findall(r'\b\d+\b', name)

    for i in digital_code:
        if len(i) == 5:
            return (i)
        else:
           return ("brak kodu")


for i in range(pages):
    number += 1
    for offers in soup.find_all('div', {'data-cy' : 'l-card'}):
        link_offer = offers.find('a', {'class' : 'css-rc5s2u'})
        name = offers.find(class_='css-16v5mdi er34gjf0')
        name = name.get_text()
        digital_code = str(checker(name))
        if digital_code != "brak kodu":
            link2 = requests.get('https://zklockow.pl/lego-' + digital_code)
            soup2 = BeautifulSoup(link2.text, 'html.parser')
            global_price =soup2.find(class_='WraPri')
            print(global_price.get_text())
        else:
            pass
        price = offers.find('p', {'data-testid': 'ad-price'})
        print("nazwa zestawu to : " + name + " Jego kod to: " + digital_code + " na olx kosztuje on : " + (" Ogólna cena to: ") + global_price  + " Link do strony: " + "https://www.olx.pl" + str(link_offer.get('href')))

    link = requests.get('https://www.olx.pl/dla-dzieci/zabawki/q-lego/?page=' + str(number))
    soup = BeautifulSoup(link.text, 'html.parser')

#str(price.get_text())