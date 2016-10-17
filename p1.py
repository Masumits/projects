import urllib.request
import re   
import os
import html

def download_page(pageUrl):
        try:
            page = urllib.request.urlopen(pageUrl)
            text = page.read().decode('ISO-8859-1')
        except:
            text = 'Nopage'
            return text
          
def findtext(text):
    regPosttext = re.compile('<div class="entry-content">(.*?)</div><!-- .entry-content -->', flags=re.U | re.DOTALL)
    rPtx = regPosttext.search(text) 
    if rPtx:
        find_text = rPtx.group(1)
    else:
        find_text = 'Noname'   
    return find_text

    
def author_name(text):
    regPostauthor = re.compile('rel="author">(.*?)</a></span>', flags=re.U | re.DOTALL)
    rPa = regPostauthor.search(text) 
    if rPa:
        author = rPa.group(1)
    else:
        author = 'Noname'   
    return author


def header_title(text):
    regPosttitle = re.compile('<title>(.*?)\|', flags=re.U | re.DOTALL)
    rPt = regPosttitle.search(text) 
    if rPt:
        title = rPt.group(1)
    else:
        title = 'Notitle'     
    return title


def find_date(text):
    rex = re.compile('datetime="(([0-9]{4})\-([0-9]{2})\-([0-9]{2}))')
    m = re.search(rex,text )
    if m:
        date = m.group(4) + '.' + m.group(3) + '.' + m.group(2)
        month = m.group(3)
        year = m.group(2)
    else:
        date = 'Nodate'
        month ='Nomonth'
        year = 'Noyear'
    return (date, year, month)
    
def dirs(i, year, month, author, title, date, pageUrl, find_text):
    if not os.path.exists('C:\\Users\\North Star\\YandexDisk\\proekt\\plain'+ os.sep + year + os.sep + month):
        os.makedirs('C:\\Users\\North Star\\YandexDisk\\proekt\\plain'+ os.sep + year + os.sep + month)
    path = 'C:\\Users\\North Star\\YandexDisk\\proekt\\plain'+ os.sep + year + os.sep+ month+ os.sep + str(i) + ".txt"
    f = open(path, 'w', encoding = 'utf-8')
    f.write ('@au ' + author + '\n' + '@ti ' + title + '\n' + '@da ' + date +  '\n' + '@url ' + pageUrl + '\n'  + find_text)
    f.close()
    print(i)
    return path

def meta_data(path, author, title, date, pageUrl, year):
    metadata = open('C:\\Users\\North Star\\YandexDisk\\proekt\\proekt.csv','a',encoding = 'utf-8')
    row = '%s\t%s\t\t\t%s\t%s\t\tпублицистика\t\t\tнет категории\t\tнейтральный\tн-возраст\tн-уровень\tреспубликанская\t%s\t\tТуваОнлайн\t%s\t\tгазета\tРоссия\tРеспубликаТува\tru'
    metadata.write(row % (path, author, title, date, pageUrl, year) + "\n")
    metadata.close()  

    
def main():
    commonUrl = 'http://tuvpravda.ru/?p='
    for i in range(1, 577):
        pageUrl = commonUrl + str(i)
        try:
            page = urllib.request.urlopen(pageUrl)
            text = page.read().decode('utf-8')            
        except:
            print('Error at', pageUrl)
            continue
        find_text = findtext(text)
        author = author_name(text)
        title = header_title(text)
        pageUrl = download_page(text)
        (date, year, month) = find_date(text)
        path = dirs(i, year, month, author, title, date, pageUrl, find_text)
        meta_data(path, author, title, date, year, pageUrl)
   

if __name__ == '__main__':
    main()
