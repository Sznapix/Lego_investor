import  re
from bs4 import BeautifulSoup
import requests
import mysql.connector
digital_number = ["2137","666","42042","1611","55555"]
napis = "tutaj 22 jest 42322 sciernisko 23 o kurde 23325 32"
x = re.findall(r'\b\d+\b', napis)

"""def checker(napis):
    x = re.findall(r'\b\d+\b', napis)
    for i in x:
        if len(i) == 5:
            print("to jest kod")
        else:
            print("to nie jest kod")
#checker(napis)

#link2 = requests.get("https://zklockow.pl/lego-10283-wahadlowiec-discovery-nasa")
#soup2 = BeautifulSoup(link2.text, 'html.parser')
#print(soup2.get_text())
#global_price =soup2.find(class_='table table-hover ctlsets-table')
#print(global_price)

connection = mysql.connector.connect(user="root", host='localhost', password=None, database='baza_ofert_lego', auth_plugin="mysql_native_password")
cursor = connection.cursor()
query= "INSERT INTO oferty (offer_name, digital_number, link, offer_price, global_price) VALUES ('{}',{},'{}',{},{})".format('d222',22,"testujemy222",223,233)
cursor.execute(query)

connection.commit()
connection.close()
"""
choice = str(input("Podaj swój wybór"))
match choice:
    case 'ddd':
        print("test1")
    case 'jddd':
        print("test2")
