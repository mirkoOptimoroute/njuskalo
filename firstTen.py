from __future__ import print_function
from bs4 import BeautifulSoup
import requests


page = requests.get('http://www.njuskalo.hr/iznajmljivanje-poslovnih-prostora')
soup = BeautifulSoup (page.content, 'lxml')
elements = []

for li in soup.find_all('article'):
    data = []
    #print(li.find('a').text)
    for child in li.children:
        if child.name == 'h3':
            for ch in child.children:
                if ch.name == 'a':
                    data.append(ch.text)
                    article = ch.parent.parent 
                    #soup2 = BeautifulSoup (article, 'lxml')
                    #soup2.find_all(class = 'price')                       
                    for entityPrice in article.descendants: 
                        if entityPrice.name:
                            if 'class' in entityPrice.attrs:
                                if entityPrice['class'][0] == 'price':
                                    data.append(entityPrice.text)
                    elements.append(data)

for i in range(min(len(elements), 10)):
    print ('Naslov: ' + elements[i][0])
    if len(elements[i]) >= 1:
        print ('Cijena: ' + elements[i][1], end = ' ') 
        for j in range (2, len(elements[i])):  
            print(elements[i][j][:-1], end=' ')
        print()

