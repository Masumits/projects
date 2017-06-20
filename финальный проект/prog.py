import textGen as tg
import random
import pymorphy2
from pymorphy2 import MorphAnalyzer
import linecache

morph = MorphAnalyzer()#создали экземпляр класса морф

#функция для получения случайного слова из файла
def getWord():
    m = random.randint(1, 1054206)
    line = linecache.getline('words.txt', m)
    word = line.split()[0]
    return word

#получаем наречие
def get_adverb():
    while True:
        new_word = getWord()#кладём в переменную случайное слово
        ana = morph.parse(new_word)[0]#получаем его самый частотный разбор
        if 'ADVB' in ana.tag:
            break
    return new_word


#получаем числительное
def get_numr():
    while True:
        new_word = getWord()
        ana = morph.parse(new_word)[0]
        if 'NUMR' in ana.tag:
            break
    return new_word


#получаем существительное в им.падеже
def get_noun_nomn():
    while True:
        new_word = getWord()
        ana = morph.parse(new_word)[0]
        if {'NOUN', 'anim', 'nomn', 'sing'} in ana.tag:
            break
    return new_word

#получаем сущ в вин
def get_noun_accs():
    while True:
        new_word = getWord()
        ana = morph.parse(new_word)[0]
        if {'NOUN', 'accs'} in ana.tag:
            break
    return new_word


#получаем сущ в предложном
def get_noun_loct():
    while True:
        new_word = getWord()
        ana = morph.parse(new_word)[0]
        if {'NOUN', 'loct'} in ana.tag:
            break
    return new_word


#получаем сущ в родительном
def get_noun_gent():
    while True:
        new_word = getWord()
        ana = morph.parse(new_word)[0]
        if {'NOUN', 'gent'} in ana.tag:
            break
    return new_word

#обработка пользовательского ввода
def gen_sent_final(word):
    model = tg.train('d.txt')
    
    test_word = word.lower().split()[0]#берём первое слово в введённом предложении и делаем его маленькими буквами
    tst = morph.parse(test_word)[0]

    marker = False

    #каждый блок == обработка определённого кейса

    #Обрабатываем вариант с "почему"
    if test_word == 'почему':
        marker = True
        if random.random() < 0.5:
            word = 'потому что'
        else:
            word = 'так как'

    if test_word == 'зачем':
        marker = True
        word = 'затем что'

    if test_word == 'как':
        marker = True
        word = get_adverb()

    if test_word == 'сколько':
        marker = True
        word = get_numr()

    if test_word == 'кто':
        marker = True
        word = 'это был(а) ' + get_noun_nomn()

    if test_word == 'куда':
        marker = True
        if random.random() < 0.5:
            word = 'туда куда'
        else:
            word = 'в ' + get_noun_accs()

    if test_word == 'где':
        marker = True
        word = 'в ' + get_noun_loct()

    if test_word == 'какой':
        marker = True
        if random.random() < 0.5:
            word = 'тот который'
        else:
            word = 'такой что'

    if test_word == 'что':
        marker = True
        word = get_noun_accs()

    if test_word == 'откуда':
        marker = True
        word = 'из ' + get_noun_gent()

    if 'PREP' in tst.tag:
        marker = True
        word = test_word + ' ' + get_noun_loct()

    if test_word == 'когда':
        marker = True
        word = 'тогда когда'

    #######################################################################
    if not(marker):

        if random.random() < 0.5:            
            if random.random() < 0.5:
                word = 'Да,'
            else:
                word = 'Нет,'
        else:
            word = test_word
        
            

    return tg.gen_sent(model, word)


#print(gen_sent_final('ывфдлаыдлфвоа'))
















