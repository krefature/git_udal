f = open('Perepis.txt', 'r+')
summa=0
with open('Perepis.txt') as f:
    for i in f:
        chislo=int(i[-5:-1])
        if chislo<1978:
            print(i[:-13])
            summa+=1
    print(summa)
f.close()