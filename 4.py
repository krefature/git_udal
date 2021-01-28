f = open('Perepis.txt', 'r+')
u1=int(input())
u2=int(input())
summa=0
with open('Perepis.txt') as f:
    for i in f:
        chislo=int(i[-5:-1])
        if chislo<1978:
            print(i[:-13])
            summa+=1
    print(summa)
    for i in f:
        chislo=int(i[-5:-1])
        if chislo<u2 and chislo>u1:
            print(i[:-13])
f.close()