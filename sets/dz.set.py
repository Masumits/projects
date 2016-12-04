import urllib.request, re, html
def links():
    f = open('статьи.csv', 'r', encoding = 'UTF-8')
    link = []
    for m in f:
        link.append(m)
    f.close()
    return link
    
def reg(link):
    filer = ['<p>(.*?)</em></p>', '</strong>(.*?)<div class="author_tags_block">','<p><strong>(.*?)</p>\n<p><strong>', '<span class="_ga1_on_ include-relap-widget contextualizable">(.*?)</span>'] 
    tex = []
    for i,u in enumerate(link): 
        page = urllib.request.urlopen(u) 
        try: 
            htl = page.read().decode('utf-8') 
        except: 
            htl = page.read().decode('windows-1251')
        r = re.compile(filer[i], flags=re.U | re.DOTALL)
        regex = re.search(r,htl)
        if regex:
            n = regex.group(1)
            regTag = re.compile('<.*?>', flags=re.U | re.DOTALL)            
            regSpace = re.compile('\s', flags=re.U | re.DOTALL)
            n = regTag.sub('', html.unescape(n))
            n = regSpace.sub(' ', n)
            nr = n.split()
            for i,i1 in enumerate(nr):
                nr[i] = i1.strip('©.,?!:;()- — \"\'\«\»')
                nr[i] = nr[i].lower()   
            tex.append(nr)
    print (tex)
    return tex
         
def wordsets(tex):
    sets = []
    for elem in tex:
        sets.append(set(elem))
    return sets

def words(tex):
    d = {}
    for elements in tex:
        for element in elements:
            if element in d:
                d[element] += 1
            else:
                d[element] = 1
    print(d)
    return d

def intersection(sets):
    filefile = open('intersection.txt', 'w', encoding = 'UTF-8')
    inter = sets[0] & sets[1] & sets[2] & sets[3]
    for word in sorted(inter):
        filefile.write(word + '\n')
    filefile.close()
    
def symmetry(sets, d):
    filefiler = open('symmetry.txt', 'w', encoding = 'utf-8')
    sym = sets[0] ^ sets[1] ^ sets[2] ^ sets[3]
    for wordr in sorted(sym):
        if d[wordr] > 1:
            filefiler.write(wordr + '\n')
    filefiler.close()

    
def main():
    a = links()
    b = reg(a)
    c = wordsets(b)
    e = words(b)
    f = intersection(c)
    g = symmetry(c,e)
    
if __name__ == '__main__':
    main()

