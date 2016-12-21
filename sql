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
    file = open('vod_tower.sql',  'a', encoding = 'utf-8')
    file.write('CREATE TABLE lemmas (id INTERGER PRIMARY KEY, wordform VARCHAR(100), lemma VARCHAR(100);\n')
    i = 0
    lns = fi.readlines()
    #arr = {}
    for line in lns:
        a = re.search('(.*?){(.*?)}', line)
        wordform = a.group(1)
        lemma = a.group(2)
        #arr[wordform] = i
        file.write('INSERT INTO lemmas (id, wordform, lemma) VALUES (' + str(i) + ', ' + wordform.lower()+', ' + lemma.lower()+');\n')
        i += 1
    #print (arr)
    file.close()
    return file


def main():
    my__stem(start())
    file = FirstTable()
    
    
if __name__ == '__main__':
    main()
