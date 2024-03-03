import time
import sys
import math
import random

powt=1000
N=10000
def forStatement():
    k1=[]
    for i in range(N):
        k1.append(i)
    #sum_for(k1)
    #sum(k1)
    #add(k1)
    return k1

def listComprehension():
    k2=[i for i in range(N)]
    #sum_for(k2)
    #sum(k2)
    #add(k2)
    return k2

def mapFunction():
    k3=map(lambda x:x*2,range(N))
    #list(k3)
    #sum_for(k3)
    #sum(k3)
    #add(k3)
    

def generatorExpression():
    k4=(i for i in range(N))
    #list(k4)
    #sum_for(k4)
    #sum(k4)
    #add(k4)

def tester(funct):
    a=time.time_ns()
    for i in range(powt):
        funct()
    b=time.time_ns()
    return b-a

def sum_for(kk):
    suma=0
    for i in kk:
        suma+=i



print(sys.version)
test=(forStatement, listComprehension, mapFunction, generatorExpression)
for testFunction in test:
    print(testFunction.__name__.ljust(20), '=>', tester(testFunction))
def f(x): 
    if math.hypot(*x)<=1: 
        return True 
    else:
        return False
#zadanie 3
#hybot
#pi=tk/tkw razy pk/r2a
a=len(list(filter(f,[(random.uniform(0,1),random.uniform(-1,1)) for i in range (1000000)] )))
pi=(a/1000000)*4/1
print(pi)
#zadanie3

def fun3(a,b):
    d=sum(map(lambda x:(x-sum(a)/len(a))**2,a))
    a_1=sum(map(lambda x,y:(y*(x-sum(a)/len(a))),a,b))/d
    b_1=sum(b)/len(b)-a_1*sum(a)/len(a)
    y_o=math.sqrt(sum(map(lambda x,y:(y-(a_1*x+b_1))**2,a,b))/len(a))
    a_o=y_o/math.sqrt(d)
    b_o=y_o*math.sqrt(1/len(a)+(sum(a)/len(a))/d)
    return a_1,a_o,b_1,b_o
score=fun3([0,1,2],[0,1,2])
print(score)



#zadanie4
def myreduce(funct,sekw):
    sekw[0]=funct(sekw[0],sekw[1])
    del(sekw[1])
    if len(sekw)==1:
        return sekw[0]
    else:
        return myreduce(funct,sekw)


#zadanie4


a=myreduce(lambda x,y:x+y,[1,2,3,4,5])
#print(a)
b=myreduce(lambda x,y:x*y,[1,2,3,4,5])
#print(b)

#zadanie5
n=4
matrix=[[random.randint(0,20) for j in range(n)] for i in range(n)]
print(matrix)
wiersz=map(lambda x:max(x),matrix)
for el in wiersz:
    print(el)

print('Najwieksze elementy w kolumnach')
kolumna=map(lambda x:max(x),zip(*matrix))
for el in kolumna:
    print(el)

matrix_two=[[random.randint(0,20) for j in range(n)] for i in range(n)]
pudelko=[matrix,matrix_two]
print(matrix_two)
print('suma')
suma=[list(map(lambda x:sum(x),zip(matrix[i],matrix_two[i]))) for i in range(n)]
print(suma)
#suma=[list(map(lambda x:sum(x),zip(pudelko[j][i] for j in range(len(pudelko))))) for i in range(n)]
#print(suma)