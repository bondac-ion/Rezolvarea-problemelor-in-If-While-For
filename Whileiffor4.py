"""Sa se scrie un program care va efectua:
a)adunarea a 2 fractii date;
b)inmultirea a 2 fractii date;
Rezultatul va fi o fractie ireductibila"""
a=eval(input("dati un numar:"))#numarator
b=eval(input("dati un numar:"))#numitor
c=eval(input("dati un numar:"))#numarator
d=eval(input("dati un numar:"))#numitor
e=(a*d+c*b)
f=b*d
g=a*c
from  fractions import Fraction
if b!=0 or d!=0:
    print("suma este =",Fraction(e,f))
    print("produsul este =",Fraction(g,f))
else:
    print("impartirea la 0 nu are sens")