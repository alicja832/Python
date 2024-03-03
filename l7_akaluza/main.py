import random
import matplotlib
def genx(n):
    for i in range(n):
        k=[0,1,0]
        #k2=[sum(k[j-1],k[j]) for j in range(1,n)]
        #yield k2,sum(k2)
        #k=k2
#for i in genx(3):
    #print(i)
#2
def gen4(s):
    k=[]
    k=[i for i in range(len(s)) if s[i]==1]
    for i in range(1,len(k)):
        yield k[i]-k[i-1]-1

N=10
a=[0,1]
b=[random.choice(a) for i in range(N)]
print(b)
k=[i for i in gen4(b)]
    #print(i)
if((b.count(1)-1)):
    s=sum(k)/(b.count(1)-1)
    print(s)
#3
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)
def gen():
    n=0
    while True:
        yield fib(n)
        n=n+1

def gen2(a,param):
    for i in a:
        if param:
            if(not i%2):
                yield i
        else:
            if(i%2):
                yield i

def gen3(a,stop):
    for i in a:
        if i>stop:
            return 'blad'
        yield i

#nieparzyste
a=sum(gen2(gen3(gen(),99),True))
print(a)
#parzyste
a=sum(gen2(gen3(gen(),99),False))
print(a)

#zadanie4
def gen5(a,b=0,c=0):
    i=0
    it=1
    if(b):
        i=a
        if(b<a and c>0):
            yield
        #if(b<a and c<0):
         #   while i>0:
          #      yield float(i)
           #     i=i+c
    i=i+it
    a=b
    if(c):
        it=c
    while i<a:
        yield float(i)
        i=i+it
a=list(gen5(20,7,-5))
print(a)
#range(2,7)
#range(7)
k=[i for i in range(7,2,-2)]
print(k)
#zad 5
n=10
N=20
a=[0,1]
b=[random.choice(a) for i in range(N)]
l=0
p=0
osx=[i for i in range(n)]
osy=[]
for i in range(n):
    for i in range(N):
        if(b[i]):
            l=l+1
        else:
            p=p+1
        osy.append(p-l)
#plt.plot(osx,osy)




        
        
    
   