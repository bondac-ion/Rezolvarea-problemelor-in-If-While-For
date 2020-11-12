"""Se dau numerele m si n ,une m<n. Sa se verifice daca n este o putere a lui m."""
import math
m=int(input("dati un numar:"))
n=int(input("dati un numar:"))
if m<n:
    l=math.log(n,m)
    p=round(l)
    if (m**p)==n:
        print("da,n este putere a lui m")
    else:
        print("nu")