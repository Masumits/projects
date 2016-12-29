import urllib.request
import re
import html
import os
def download_text():
    req = urllib.request.Request('http://web-corpora.net/Test2_2016/short_story.html')
    with urllib.request.urlopen(req) as response:
        ht = response.read()
        ht = ht.decode('utf-8')
        ht = html.unescape(ht)
        res =  re.compile('\W([Сс].+?)\W',  flags=re.U | re.DOTALL)
        words = res.findall(ht)
        tex = []
        regTag = re.compile('<.*?>', flags=re.U | re.DOTALL)            
        regSpace = re.compile('[0-9]+?.*?[.,\"\'\«\»;\\:\(\)?—!/]', flags=re.U | re.DOTALL)  
        for t in words:
            clean_t = regTag.sub("",t)
            clean_t = regSpace.sub("",clean_t)
            clean_t = regTag.sub("", clean_t)
            clean_t = clean_t.replace('\xa00ff','')
            clean_t = clean_t.replace('\xa0', '')
            clean_t = clean_t.replace('\Off', '')
            clean_t = regSpace.sub(' ', clean_t)
            tex.append(clean_t)
        words = ' '.join(tex)
        our_words = words.split()
        file = open('words.txt','w',encoding = 'UTF-8')
        for word in our_words:
            file.write(word + '\n')
            print(word + '\n')
        file.close()
                
def mystem__():
    f = open('words.txt', 'r', encoding = 'UTF-8')
    inpu = 'words.txt'
    outpu = 'analise.txt'
    os.system(r'D:\mystem.exe -nid ' + inpu + ' ' + outpu)
    return outpu

def verbs():
    f = open('analise.txt', 'r', encoding = 'UTF-8')
    fr = f.read()
    reg = re.compile('(.*?){.*?=V.*?')
    regex = re.findall(reg,fr)
    for word in regex:
        print(word + '\n')
    f.close()

def sq():
    fi = open('analise.txt',  'r', encoding = 'utf-8')
    file = open('table.sql',  'a', encoding = 'utf-8')
    file.write('CREATE TABLE my_table (id INTERGER PRIMARY KEY, wordform VARCHAR(100), lemma VARCHAR(100), pos VARCHAR(100) ;\n')
    i = 0
    lns = fi.readlines()
    arr = {}
    for line in lns:
        a = re.search('(.*?){(.*?)=([A-Za-z]+?).*?}', line)
        wordform = a.group(1)
        lemma = a.group(2)
        pos = a.group(3)
        if wordform not in arr:
            arr[wordform] = i
            file.write('INSERT INTO my_table (id, wordform, lemma, pos) VALUES (' + str(i) + ', ' + wordform+ ', ' + lemma+ ', ' + pos+ ');\n')
            i += 1
        file.close()
        return arr

def main():
    download_text()
    mystem__()
    verbs()
    sq()
if __name__ == '__main__':
    main()
