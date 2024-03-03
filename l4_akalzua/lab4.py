import random
import copy
#zad.1
#Proszę utworzyć k-elementową 
#listę całkowitych wartości losowych z przedziału [0,5k).
k=1000
l1=[random.randint(0,k) for i in range (k) ]
print(l1)

#Proszę sprawdzić ile elementów pozostaje 
#na swoim miejscu po losowym przemieszaniu listy,
# mieszanie proszę wykonać 100 razy a wyniki 
#zapisywać w słowniku
l2=copy.deepcopy(l1)
s={}
for i in range(100):
    a=0
    random.shuffle(l1)
    for j in range(len(l1)):
        if l1[j]==l2[j]:
            a+=1
    s.setdefault(a,[]).append(i)

print(s)
#a = sum(j*(i - xsrednie) for i,j in lista4 )
#s=dict(sum(if l1[] lista4 ))

#drugie zadanie
#Proszę utworzyć losowy string o długości k 
#zawierający tylko małe 
#litery, pomiędzy poszczególne 
#litery proszę wstawić kropkę (

#97-122
import string 
litery=[random.choice(string.ascii_lowercase)for i in range (k)]
s=''.join(litery[:])
s=s.replace('wo','w.o')
print(s)

#zadanie 3
#Proszę utworzyć listę stu całkowitych wartości 
#losowych z przedziału [0,20). 
#Następnie na jej podstawie proszę utworzyć słownik, 
#w którym 
#klucze są liczbami z listy, 
#a wartościami lista ich indeksów.
l3=[random.randint(0,20)for i in range (100)]
s={}
for i,v in enumerate (l3):
    if v not in s:
        s[l3[i]]=i
    #else:
        #s.setdefault(l3[i],[]).append(i)
print(s)
s.clear()
#w rozwiązaniu proszę wykorzystać metody
# setdefault i index, i nie korzystać ani z range, 
#ani z enumerate (1.5p)
#s.setdefault(7,[]).append(3)
for i in l3:
    if l3[i] not in s:
        s.setdefault(i,[]).append(l3.index(i)) 
    #else:
        #s.setdefault(i,[]).append(l3.index(i)) 
print(s)
#zad4
a={}

a=dict((len(str(random.randint(0,k))),2)for j in range (1000) if len(str(random.randint(0,k)))<6 and len(str(random.randint(0,k)))>3 )
