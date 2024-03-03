import matplotlib.pyplot as plt
import numpy
x,y,z=numpy.loadtxt('zad3.txt', unpack=True)
plt.errorbar(x, y, marker='*', yerr=dy)
plt.xlabel('x')
plt.savefig('res.pdf')