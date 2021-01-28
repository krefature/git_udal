f = open('travels.txt', 'r+')
summa1=0
summa2=0
summa3=0
slova=0
s=0
massa1=0
massa2=0
massa3=0
with open('travels.txt') as f:
    for i in f:
        chislo=int(i[:1])
        if chislo==1:
            summa1+=1
            S=int(i[-11:-7])
            s+=S
            massa1+=int(i[-4:])
        elif chislo==2:
            summa2+=1
            massa2+=int(i[-4:])
        elif chislo==3:
            summa3+=1
            massa3+=int(i[-4:])
    print(s)
    if summa1>summa2 and summa1>summa3:
            print('1')
    elif summa2>summa1 and summa2>summa3:
            print('2 больше,','всего масса=',massa2)
    else:
            print('3')
f.close()
with open('travels.txt') as f:
    for i in f:
        slovo=i[10:15]
        if slovo=='Липки':
            slova+=1
    print(slova)

f.close()