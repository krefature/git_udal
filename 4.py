f=open('Perepis.txt','r+')
with open('Perepis.txt') as f:
    l=f.readlines()
    for i in range(1,len(l)):
        print(l[i])
        s=str(l[i])
        a=s[len(s)-5:len(s)+1]
        spis=[]
        spis=a.split()
        year=int(spis[0])
        print(year)


