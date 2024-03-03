import sys
import random
import time
sys.path.append("build/lib.linux-x86_64-3.10")
import mod
a=mod.met(1,2)
print(a)
a=mod.met(1,2,5)
print(a)
a=mod.met(1,2,5,[2,3,4])
print(a)

a=[1,10,2]
b=mod.sort_one(a,3)
print(b)
def sort_onee(A,n):
    "'function'"
    for i in range (n):
        k = A[i]
        j = i - 1
        while (j>0 and A[j]>k):
            A[j+1]=A[j]
            j = j - 1
     
        A[j + 1] = k


x=time.time_ns()
r=[10,10**2,10**3,10**4]
for j in r:
    a=[random.randint(0,j) for i in range(j)]
    mod.sort_one(a,j)
b=time.time_ns()
print(b-x)
x=time.time_ns()
r=[10,10**2,10**3,10**4]
for j in r:
    a=[random.randint(0,j) for i in range(j)]
    sort_onee(a,j)
b=time.time_ns()
print(b-x)
#zadanie3
s={1:2}
