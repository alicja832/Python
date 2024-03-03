import glob
import re
import numpy
#kolejnosc jest nieokreslona
def fun(name,n):
    with open(name) as pl:
        lis=pl.readlines()
        print(lis[:n])
        print(lis[-n:])
        print(lis[::n])
        for i in lis:
            if n<len(i):
                print(re.split(' ',i)[0])


                #lista=re.split(' ',line)
                #print(lista[n])
                #line=pl.readline()     
fun('my_file.txt',1)
#zadanie 2

lista_nazw=glob.glob('data*in')
s={}
for i in lista_nazw:
    j=0
    with open(i) as pl:
        line=pl.readline()
        while line:
            s.setdefault(j,[]).append(float(line))
            line=pl.readline()
            j+=1
zapis=open('zad2.txt','w')

for i in s:
    zapis.write(f'{i}')
    zapis.write(' ')
    zapis.write(f'{numpy.average(s[i])}')
    zapis.write(' ')
    zapis.write(f'{numpy.std(s[i])}')
    zapis.write('\n')
zapis.close()

#zadanie3
zapis=open('zad3.py','w')
zapis.write("import matplotlib.pyplot as plt\nimport numpy\nx,y,z=numpy.loadtxt('zad3.txt', unpack=True)\nplt.errorbar(x, y, marker='*', yerr=dy)\nplt.xlabel('x')\nplt.savefig('res.pdf')")
#zadanie 4
zapis=open('rank.out','w')
lista_nazw=glob.glob('2*.txt')
zapis.write('Nazwisko ')
s={}
for i in lista_nazw:
    zapis.write(i[:4])
    zapis.write('  ')
    with open(i) as pl:
        line=pl.readline()
        while line:
            s.setdefault(re.split(' ',line)[0],[]).append(int(re.split(' ',line)[1]))
            line=pl.readline()
        #s.setdefault(j,[]).append(float(line)
zapis.write('\n')
for i in s:
    zapis.write(i)
    zapis.write('     ')
    for j in s[i]:
        zapis.write(f'{j}')
        zapis.write('    ')
    zapis.write('\n')
print(s)