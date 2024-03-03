import math
from cmath import sqrt as csqrt

#zachodzi konwersja z str do float 
a = float(input('a=?'))
b = float(input('b=?'))
c = float(input('c=?'))

d = b*b - 4*a*c
if abs(d) <= 1e-6:
 x = -b/(2*a)
 print(f'x = {x:.3f}')
elif d > 1e-6:
 x1 = (-b-math.sqrt(d))/(2*a)
 x2 = (-b+math.sqrt(d))/(2*a)
 print(f'x1 = {x1:.3f},x2 = {x2:.3f}')
else :
 x1 = (-b-csqrt(d))/(2*a)
 x2 = (-b+csqrt(d))/(2*a)
 print(f'x1 = {x1:.3f}, x2 = {x2:.3f}')