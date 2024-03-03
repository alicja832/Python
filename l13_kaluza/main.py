
from dataclasses import dataclass
import typing
import glob
import os
import json
import sys
#Klasę implementującą stos, który można zainicjalizować 
#przekazując zmienną liczbę parametrów, listę lub inny stos. 
#Sprawdzenie typu i odpowiednią inicjalizację proszę wykonać 
#korzystając z konstrukcji match-case. W klasie proszę zdefiniować 
#metodę pozwalającą na dodanie elementu do stosu oraz 
#metodę pozwalającą na jego wypisanie. Proszę przetestować działanie klasy (2p).
class Stack:
    def __init__(self,*par):
        self.stack=[]
        #print(type(*par))
        match type(*par):
            case list():
                print("lista")
                for i in par:
                    self.stack.append(i)
            case tuple():
                print("tuple")
                for i in par:
                    self.stack.append(i)
            case int():
                print("int")
                self.stack.append(i)
   # def add(self,el):


a=Stack([1,2,3])

#zadanie 2
#klasy z dekoratorem opisujace pracownikow o oferty pracy nazwiko wikkkk
@dataclass
class Pracownik:
    nazwisko:str
    wiek:int
    wyksztalcenie:str

@dataclass 
class Oferta:
    opis:str
    wiek:int
    wyksztalcenie:str

def fun():
    plik=glob.iglob('*.json')
    with open(plik) as pl:
        pass

ob=Pracownik('Kowalski',18,'inz')
print(ob)
def fun():
    if sys.argv[0]:
        print(os.path.isfile("plik.json"))
        pl=open("plik.json",'w')
        json.dump([('Sprzataczka',18,'brak'),('ksiegowa',25,'UeK')],pl)
    #json.dump(['Piekarz',30,'high school'],pl)
        pl.close()
fun()
pl=open("plik.json",'r')
a=json.load(pl)
ofert=[]
for i in a:
    print(i)
    ob=Oferta(*i)
    ofert.append(ob)

print(ofert)
print(a)



