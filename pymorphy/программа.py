import pymorphy2
from pymorphy2 import MorphAnalyzer
import random
import linecache
import re

morph = MorphAnalyzer()


def getWord():
    m = random.randint(1, 1054206)
    line = linecache.getline('words.txt', m)
    word = line.split()[1]
    return word

counter = 0

def mapWord(a):
    ana = morph.parse(a)\


    #w  = random.randint(0, len(ana) - 1)
    #если хотим выбирать случайный разбор из всех возможных
    
    ana = ana[0]
    tags = set(re.split(' |,', str(ana.tag)))

    pos = ana.tag.POS

    if pos == 'CONJ':
        return a

    if pos == 'NPRO':
        return a

    if pos == 'PREP':
        return a

    marker = True
    
    while marker:
        global counter
        counter = counter + 1
        
        word = getWord()
        ana_word = morph.parse(word)[0]
        tags_word = set(re.split(' |,', str(ana_word.tag)))
        
        if tags == tags_word:
            marker = False

    return word

x = input()
x = x.split()

responce = ''

for k in range(0, len(x)):
    responce = responce + ' ' + mapWord(x[k])

print(responce)
print('It took ' + str(counter) + ' steps to find the correct combination')
