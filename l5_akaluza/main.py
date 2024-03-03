import sys
import random
import string
def fun1(s):
    a='x'
    l=[i for i in s if i.isupper() or i.islower() and i!=a]
    print(l)
    l1=''.join(l)
    m=[f'{random.randrange(0,10,1)}' for i in l]
    m1=''.join(m)
    s2=s.maketrans(l1,m1)
    ss=s.translate(s2)
    print(ss)
    retur=[]
    for i in range (10):
        x=(random.random())
        retur.append((x,eval(ss)))
    return retur
    
list_one=fun1(sys.argv[1])
print(list_one)
   

#zad2
def fun2(*d):
    k=len(d)
    for i in range(k-1):
        for i,v in enumerate (d[(i+1):]):
            retur=[d[i][j] for j in range(len(d[i])) if d[i][j]]
        print(retur)
fun2([2,3],(1,2))

#zadanie 3
def fun3(a,b,k=True):
    if k:
        l=len(a)
    else:
        l=len(b)
    list_two=[ (a[i],b[i]) for i in range(l) if(k)]
    return list_two
list_three=fun3([2,6,7],[5,4,3])
print(list_three)

#zadanie 4
def fun4(a=(10,5,2)):
    lista_wyd=[]
    k=a[0]
    lista_wyd.apend[a[1]]
    fun4(k-a[1],a[1],a[2])