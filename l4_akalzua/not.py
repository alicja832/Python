#kluczy nie modyfikujemy
#kluczem nie moze nie bedzie lista
#kluczem moze byc krotka ale taka ktora nie zawiera obiektow modifikowalnych
s={}
s[7]=6
print(s)
#klucze nie moga sie powtarzac

#nie zmodyfikuje jesl klucz istnieje i w dodatku przypisze wart


w=s.setdefault(7,None)
print(w)
s={}
s.setdefault(7,[]).append(3)
print(s)
s={}
#to co dodajemy to dwuelementowe krotki

s=dict((k,k+1)for k in range(5))
print(s)
#typ set- to jest zbior!!!,gdy robimy s={(k,1)...}
#uzywamy klucza jako modyfikatora
print(s.keys())
#mozemy sprawdzic czy wystepuje dany klucz w slowniku
#jezeli istnieje dany klucz to musimy zrobic tak
del(s[3])
#jesli klucza nie ma to.. jak robimy s.get(10)-None,
#s.pop(10)-zdejmowanie
#s.clear()
#chce zeby mi zostal adres ale chce pozbyc sie zawartosci
#metoda update modyfikuje objekt na ktorym wywolujemy
#s2|s1 - to samo co update zwraca ale nie modyfikuje oryginalnych obiektow
#k= random.randrange([0,]7[,2])
#populacja-zestaw wartosci
#choice- losujemy cos
#k-mniejsze niz rozmiar populcji
#szukamy elementow z powtorzeniami
