#mamy dynamiczne typowanie
#parametry pozycyjne -sama nazwa bez znaku innego
#lancuch dokumentacyjny
#taki parametr z gwiazdka moze byc tylko na koncu i tylko jeden
def fun(a,*b):
    '''lancuch dokumentacujny'''
    print(b)

fun(2,'s',2,'n',[1,3])
#ze slowem kluczowym || wartoscia domyslna
def fun2(**d):
    print(d)
fun2(a=2,b=3)
#nazwane musza byc po nienazwanych
#jesli jest * to wszystko na prawo od niej musi miec podana nazwe-parametr 
def fun3(a,b,*,c):
    print(b)
fun3(2,3,c=4)
#jak jest w wowolaniu *b to nie moze byc juz samej gwiazdki
#gwiazdka w sygnaturze ale w wywolaniu tez, jak chcemy wylaczyc wartosc z np krotki,listy, ale musi byc
# mozna zrobic tak: fun((4,))-wtedy a pierwszy parametr bedzie krotka
#czy po wyjsciu z funkcji rzeczy beda sie modyfikowac?
#nie ma klasycznego przeciazenia czyli
def fun(a):
    print(a)
def fun(a,b):
    print(a)
#zwracam wartosc None
fun(3,4)
#z roznych miejsc rozne typy mozemy zwracac
#zwracam krotke ktora przechwyje 
#!a:=radom(1,10)%2 zapisuje i sprawdzam
#zmienna najpierw jest poszukiana wewnatrz funkcji pozniej na zewnatrz
x=4
a=4
print(eval('2+a*x'))