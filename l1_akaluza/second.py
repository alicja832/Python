import sys
import math
import cmath

if len(sys.argv)!=5:
 sys.exit()
#koncze program, gdy jest samo exit() to wyjdziemy tylko z intepretera

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])
d = float(sys.argv[4])

#d to zmienna ktora mi sie przyda tylko tutaj
if (d:=b**2 - 4*a*c) > eps:
 x1 = (-b-math.sqrt(d))/(2*a)
 x2 = (-b+math.sqrt(d))/(2*a)
print(f'x1 = {x1:.3f},x2 = {x2:.3f}')
elif math.fabs(d) <=eps:
 x = -b/(2*a)
 print(f'x = {x:.3f}')
else :
 x1 = (-b-cmath.sqrt(d))/(2*a)
 x2 = (-b+cmath.sqrt(d))/(2*a)
 print(f'x1 = {x1:.3f}, x2 = {x2:.3f}')