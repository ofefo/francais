#!/usr/bin/env python

import urllib.request, re, io
from gtts import gTTS
from bs4 import BeautifulSoup
from pydub import AudioSegment
from pydub.playback import play


url = 'https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard'
html = urllib.request.urlopen(url).read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')

title = soup.find('h1', {'id':"firstHeading"})
intro = soup.find('div', {'id':"mw-content-text"})
text = str()

print('\nVoici un article au hasard:\n')
print(title.get_text())
if intro.find('div', {'class':"bandeau-cell"}) is not None:
    for el in intro.find_all('p')[1:]:
        text = text + el.get_text()
else:
    for el in intro.find_all('p'):
        text = text + el.get_text()
print(text)

tts = gTTS(text, lang='fr')
tts.save('wiki.mp3')
mp3 = 'wiki.mp3'
sound = AudioSegment.from_mp3(mp3)
play(sound)
