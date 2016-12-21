import os, re

def start():
    f = open('tower.txt', 'r', encoding = 'utf-8')
    text = f.read()
    f.close()
    return text

def my__stem(text):
    inpu = 'tower.txt'
    outpu = 'vod_tower.txt'
    os.system(r'D:\mystem.exe -nd ' + inpu + ' ' + outpu)

def FirstTable():
    fi = open('vod_tower.txt',  'r', encoding = 'utf-8')
    file = open('tower.sql',  'a', encoding = 'utf-8')
    file.write('CREATE TABLE lemmas (id INTERGER PRIMARY KEY, wordform VARCHAR(100), lemma VARCHAR(100);\n')
    i = 0
    lns = fi.readlines()
    arr = {}
    for line in lns:
        a = re.search('(.*?){(.*?)}', line)
        wordform = a.group(1)
        lemma = a.group(2)
        if wordform not in arr:
            arr[wordform] = i
            file.write('INSERT INTO lemmas (id, wordform, lemma) VALUES (' + str(i) + ', ' + wordform.lower()+', ' + lemma.lower()+');\n')
            i += 1
    file.close()
    return arr


def SecondTable(arr,text): 
    file = open('tower.sql',  'a', encoding = 'utf-8')
    file.write('CREATE TABLE words(id INTERGER PRIMARY KEY, word VARCHAR(100), lemID VARCHAR(100), N VARCHAR(100);\n')
    words = text.split(' ')
    i1 = 0
    for i,word in enumerate(words):
        words[i] = word.strip('\n,.f ')
        for el in arr:
            if el == word:
                file.write('INSERT INTO words (id, word, lemID, N) VALUES (' + str(i1) + ', ' + word + ', ' + str(arr[el]) + ', '+ str(i1+1)+ ');\n')
                i1+=1
    file.close()
    #f.close()
        #return arr


def main():
    my__stem(start())
    arr = FirstTable()
    q = SecondTable(arr, start())
    
    
if __name__ == '__main__':
    main()