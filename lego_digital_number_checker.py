import  re
from bs4 import BeautifulSoup
import requests
digital_number = ["2137","666","42042","1611","55555"]
napis = "tutaj 22 jest 42322 sciernisko 23 o kurde 23325 32"
x = re.findall(r'\b\d+\b', napis)

def checker(napis):
    x = re.findall(r'\b\d+\b', napis)
    for i in x:
        if len(i) == 5:
            print("to jest kod")
        else:
            print("to nie jest kod")
#checker(napis)

link2 = requests.get("https://zklockow.pl/lego-10283-wahadlowiec-discovery-nasa")
soup2 = BeautifulSoup(link2.text, 'html.parser')
global_price =soup2.find(class_='WraPri')
print(global_price.get_text())
#global_price =soup2.find(class_='table table-hover ctlsets-table')
#print(global_price)
