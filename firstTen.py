from __future__ import print_function
from bs4 import BeautifulSoup
import requests

class Element:
    naslov = ""
    cijena = []

def find_all_elements (elements, soup):
    #elements = []
    element = Element()
    for li in soup.find_all('article'):
        data = []
        #print(li.find('a').text)
        for child in li.children:
            if child.name == 'h3':
                for ch in child.children:
                    if ch.name == 'a':
                        #data.append(ch.text)
                        #print(ch.text)
                        element.naslov = ch.text
                        article = ch.parent.parent 
                        #soup2 = BeautifulSoup (article, 'lxml')
                        #soup2.find_all(class = 'price')                       
                        for entityPrice in article.descendants: 
                            if entityPrice.name:
                                if 'class' in entityPrice.attrs:
                                    if entityPrice['class'][0] == 'price':
                                        #data.append(entityPrice.text)
                                        element.cijena.append(entityPrice.text)
                        elements.append(element)
    return elements

elements = []
urls = ['http://www.njuskalo.hr/iznajmljivanje-poslovnih-prostora',
'http://www.njuskalo.hr/iznajmljivanje-poslovnih-prostora?page=2',
'http://www.njuskalo.hr/iznajmljivanje-poslovnih-prostora?page=3',
'http://www.njuskalo.hr/iznajmljivanje-poslovnih-prostora?page=4',
'http://www.njuskalo.hr/iznajmljivanje-poslovnih-prostora?page=5',
'http://www.njuskalo.hr/iznajmljivanje-poslovnih-prostora?page=6',
'http://www.njuskalo.hr/iznajmljivanje-poslovnih-prostora?page=7',
'http://www.njuskalo.hr/iznajmljivanje-poslovnih-prostora?page=8',
'http://www.njuskalo.hr/iznajmljivanje-poslovnih-prostora?page=9',
'http://www.njuskalo.hr/iznajmljivanje-poslovnih-prostora?page=10',
'http://www.njuskalo.hr/iznajmljivanje-poslovnih-prostora?page=11',
'http://www.njuskalo.hr/iznajmljivanje-poslovnih-prostora?page=12'
]

for url in urls:
    page = requests.get(url)   
    soup = BeautifulSoup (page.content, 'lxml')
    elements = find_all_elements(elements, soup)
#print (len(elements))
#print(elements.getNaslov())
#print (elements)
#Elements u strukturu
for element in elements:
    print ('Naslov: ' + element.naslov)
    for cijena in element.cijena:
        print ('Cijena: ' + cijena, end = ' ') 
            #for k in xrange (2, len(elements[i][j])):  
             #   print(elements[i][j][k][:-1], end=' ')
        print()

