words = open('words.txt', 'w')

with open('d.txt','r') as f:
    for line in f:
        for word in line.split():
           words.write('1 ' + word + '\n')
