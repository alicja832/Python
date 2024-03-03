k=[2,3,4,2,9]
for i in k:
        if 2 in k:
            k.remove(2)
print(k)

k=[2,3,4,2,9,2,0]
while 2 in k:
    k.remove(2)
print(k)

#Korzystając z pętli for oraz funkcji range proszę wypisać co drugi element listy
# począwszy od elementu o indeksie 1 (bez instrukcji warunkowej) (0.5p)

i=0
c=1
k=[2,3,4,2,9,2,0]
for i in range(1,len(k),2):
    print(k[i],end=',')
print('\n')

for i in range(len(k)-1,-1,-2):
    print(k[i],end=',')
print('\n')
#Proszę utworzyć nową listę, której elementami są 
#krotki (indeks, element) na podstawie istniejącej listy <- lista składana (1p)
a=[]
for i,v in enumerate(k):
    a.append((i,v))
print(a)
#p.8 sortowanie

a.sort(key=lambda x: x[1])
print(a)
#zad9
b=[]
for i,v in enumerate(k):
    if not v%2:
        b.append((i,v))
print(b)

#zad 10
b=[]
for i,v in enumerate(k):
    b.append((i,v)) if i<v else b.append((v,i))
print(b)

#zadanie 11
N=4
k=[]
for i in range(N):
    tmp=[]
    for j in range(N):
        if i==j:
            tmp.append((1,1))
        tmp.append((0,0))
    k.append(tmp)
print(k)
print("Podpunkt c")
k=[]
for i in range(N):
    tmp=[]
    for j in range(N):
        if j==(i+N-1):
            tmp.append((1,1))
        tmp.append((0,0))
    k.append(tmp)
print(k)

