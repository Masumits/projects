import pymorphy2
from pymorphy2 import MorphAnalyzer
import random
import linecache
import re

morph = MorphAnalyzer()#создали экземпляр класса морф

#функция для получения случайного слова из файла
def getWord():
    m = random.randint(1, 1054206)
    line = linecache.getline('words.txt', m)
    word = line.split()[1]
    return word

counter = 0
#глобальная переменная для подсчёта количества операций

def mapWord(a):
    ana = morph.parse(a)#получаем все разборы исходного слова


    #w  = random.randint(0, len(ana) - 1)
    #если хотим выбирать случайный разбор из всех возможных
    
    ana = ana[0]#берём только первый (самый частотный) разбор  
    tags = set(re.split(' |,', str(ana.tag)))#получаем все теги как множество строк, при помощи регулярного выражения

    #в случае, если мы попали в союз или местоимение, просто выдаём их же
    pos = ana.tag.POS

    if pos == 'CONJ':
        return a

    if pos == 'NPRO':
        return a

    if pos == 'PREP':
        return a

    marker = True
    #условие выхода из цикла

    while marker:
        global counter
        counter = counter + 1
        #просто считаем количество итераций
        
        word = getWord()#генерируем новое слово
        ana_word = morph.parse(word)[0]#получаем его первый разбор
        tags_word = set(re.split(' |,', str(ana_word.tag)))#получаем множество его тегов
        
        if tags == tags_word:
            marker = False
        #если два множества тегов совпали, то выходим из цикла

    return word


def makeResponse(x):
    x = x.split()
    
    response = ''

    for k in range(0, len(x)):
        response = response + ' ' + mapWord(x[k])

    return response

