from bs4 import BeautifulSoup
import requests
import  re
import mysql.connector

connection = mysql.connector.connect(user="root", host='localhost', password=None, database='baza_ofert_lego', auth_plugin="mysql_native_password")
cursor = connection.cursor()


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
            return "brak kodu"


for i in range(pages):
    number += 1
    for offers in soup.find_all('div', {'data-cy' : 'l-card'}):
        link_offer = offers.find('a', {'class' : 'css-rc5s2u'})
        name = offers.find(class_='css-16v5mdi er34gjf0')
        name = name.get_text()
        digital_code = str(checker(name))

        if digital_code != "brak kodu" and digital_code != "None":
            link2 = requests.get("https://zklockow.pl/lego-" + digital_code)
            soup2 = BeautifulSoup(link2.text, 'html.parser')
            price = offers.find('p', {'data-testid': 'ad-price'})
            global_price = soup2.find(class_='WraPri')
            if str(global_price) != "None":
                print("nazwa zestawu to : " + name + " Jego kod to: " + str(digital_code) + " na olx kosztuje on : " + str(price.get_text()) + (" Ogólna cena to: ") + str(global_price.get_text()) + " Link do strony: " + "https://www.olx.pl" + str(link_offer.get('href')))
                query = "INSERT INTO oferty (offer_name, digital_number, link, offer_price, global_price) VALUES ('{}',{},'{}',{},{})".format(name, digital_code, "https://www.olx.pl" , 222,22)
                cursor.execute(query)
                connection.commit()
            else:
                print("Oferta nie istnieje")
        else:
            pass

    link = requests.get('https://www.olx.pl/dla-dzieci/zabawki/q-lego/?page=' + str(number))
    soup = BeautifulSoup(link.text, 'html.parser')
connection.close()