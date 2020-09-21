#!/usr/bin/env python

import urllib.request, re
from bs4 import BeautifulSoup

url = 'https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard'
html = urllib.request.urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

title = soup.find('h1', {'id':"firstHeading"})
intro = soup.find('div', {'id':"mw-content-text"})

print('\nVoici un article au hasard:\n')
print(title.get_text())
for el in intro.find_all('p'):
    print(el.get_text())
