#zad 1
import sys
import copy
if len(sys.argv)<2:
    print('Program bedzie dzialal odpowiednio jesli podasz parametry')
    sys.exit()

a=''.join(sys.argv[1:])
print(a)
#zad.2
l=[i for i in a if i.islower()]
print(l)
u=[i for i in a if i.isupper()]
print(u)
n=[i for i in a if i.isnumeric()]
print(n)
p=[i for i in a if not i.islower() and not i.isupper()]
print(p)
#zad 3
#Na podstawie utworzonej listy zawierającej małe 
#litery proszę utworzyć listę małych liter bez powtórzeń 
k=[]
for m in l:
    if m not in k:
        k.append(m)
print(k)

krotka = [(i,l.count(i)) for i in k]
print(krotka)
#zadanie 4
#Otrzymaną w powyższym punkcie listę proszę wyświetlić 
#w kolejności od najwyższej krotności (bez sortowania listy oryginalnej) (1p)
for i,j in sorted(krotka,key=lambda x:x[1],reverse=True):
    print((i,j))

print(krotka)
#Proszę utworzyć listę dwuelementowych krotek, w których pierwszy 
#element jest liczbą pobraną z listy cyfr, drugi natomiast wartością 
#funkcji liniowej ax+b dla danej liczby; wartości współczynników proszę 
#ustalić w następujący sposób: a równa się liczbie
# samogłosek w stringu z punktu pierwszego, a b - liczbie spółgłosek tamże (2p)
awsp=0
b=0
samogl = 'aeyuoAEYUO'
for i in a:
    if i in samogl:
        awsp+=1
    elif i not in n and i not in p:
        b+=1
print(awsp)
print(b)


lista4 = [(int(i),awsp*int(i)+b) for i in n]
print(lista4)

if(len(lista4)==0): len=1
else: len=len(lista4)

xsrednie= sum(i for i,j in lista4  )/len
ysrednie= sum(j for i,j in lista4  )/len

D=sum(pow((i-xsrednie),2) for i,j in lista4  )/len
if(D!=0):
    a = sum(j*(i - xsrednie) for i,j in lista4 )/D
    b =ysrednie - a* xsrednie