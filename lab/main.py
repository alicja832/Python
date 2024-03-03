#1. Korzystając z pętli for proszę usunąć wszystkie wystąpienia określonej wartości z listy
#2. j.w. ale korzystając z pętli while
#3. Korzystając z pętli for oraz funkcji range proszę wypisać co drugi element listy począwszy od elementu o indeksie 1 (bez instrukcji warunkowej)
#4. j.w. ale bez range
#5. Korzystając z pętli for oraz funkcji range proszę wypisać co drugi element listy od końca (bez instrukcji warunkowej)
#6. j.w. ale bez range
#7. Proszę utworzyć nową listę, której elementami są krotki (indeks, element) na podstawie istniejącej listy <- lista składana
#8. Proszę posortować listę z poprzedniego punktu wg drugiego elementu krotek
#9. Proszę utworzyć nową listę, której elementami są krotki (indeks, element) na podstawie istniejącej listy, przy czym dodajemy krotkę tylko, jeśli wartość pobrana z listy jest wartością parzystą <- lista składana
#10. Proszę utworzyć nową listę, której elementami są krotki (indeks, element) lub (element, indeks) na podstawie istniejącej listy, tak, aby pierwszy element krotki był mniejszy od drugiego <- lista składana
#11. Proszę utworzyć listę 2D (lista składana) wypełnioną zerami oraz jedynkami, przy czym jedynki występują:
#-w kwadracie o boku mniejszym od rozmiaru listy na jej "środku"
# -na przekątnej od lewego górnego rogu do prawego dolnego
#-na przekątnej od prawego górnego rogu do lewego dolnego
#-na obu przekątnych
#-w szachownicę
print("Zadanie pierwsze")
import random

size=20
k=[random.randrange(10) for i in range (size)]
k.append(3)

print("Przed wykonaniem selekcji")
print(k)

okreslona_wartosc=3

for i in k:
    if i==okreslona_wartosc:
        k.remove(i)

print("Po wykonaniu selekcji")
print(k)

print("zadanie drugie")
size=20
k=[random.randrange(10) for i in range (size)]
k.append(3)

print("Przed wykonaniem selekcji")
print(k)

i=0
while i<len(k):
    if k[i]==okreslona_wartosc:
        k.remove(k[i])
    i=i+1

print("Po wykonaniu selekcji")
print(k)

print("Zadanie trzecie")

for i in range(1,len(k),2):
    print(i,":",k[i])

print("Zadanie czwarte")
for i in range(len(k)-1,0,-2):
    print(i,":",k[i])

print("Zadanie siódme")
new_size=len(k)

kiel=[]
for i in range (new_size):
    kiel.append((i,k[i]))
print(kiel)

print("Zadanie ósme")

def fun(el):
    return el[1]

kiel.sort(key=fun)
print(kiel)

print("zadanie 10")

def fun_two(el):
    if(el[0]<el[1]):
        return el
    else:
        x=(el[1],el[0])
        return x
    
result=map(fun_two,kiel)
print(list(result))