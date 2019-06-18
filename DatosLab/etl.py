from bs4 import BeautifulSoup
import requests

web =  'https://ciperchile.cl/2019/03/19/menores-que-abandonan-la-escuela-fondos-publicos-para-colegios-de-reinsercion-cayeron-en-1-300-millones/'
f = etl(text = '',link = web)
f.ciper()

class etl:
    #Con __init__ comparto las variabbles en él de forma global
    def __init__(self, text, link):
        self.text = text
        self.link = link

    #Codigo adaptado para la pagina CiperChile.cl
    def ciper(self):

        noti = []  
        
        source = requests.get(self.link).text

        soup = BeautifulSoup(source, 'lxml')
        head = soup.find('h1').get_text()
        noti.append(head)

        body = soup.find('div', {'class': 'gridle-gr-10 gridle-gr-12@midlarge single__holder print-full'})

        #en news se buscan todos los tag <p> dentro del laa variable body peviamente extraida
        news =  [body.get_text() for ingredient in body.select('p')]
        noti.append(news)

        #aca self.text esta apuntando a noti[]
        self.text = noti
        print(self.text[0])

    def findCifra(self):

        for 


