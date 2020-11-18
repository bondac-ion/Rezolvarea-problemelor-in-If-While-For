"""Se da un numar natural n.Sa se compare s1 si s2."""
n=int(input("dati un numar:"))
s1=0
s2=0
for i in range(1,n+1):
    s1+=i**3
    s2+=i

if s1>(s2**2):
    print("s1",">","s2")
elif s1<(s2**2):
    print("s1","<","s2")
else:
    print("s1","=","s2")

n=int(input("dati un numar:"))
s1=0
s2=n**3+n**2
for i in range(1,n+1):
    s1+=i**2
    s2+=i

if (3*s1)>s2:
    print("s1",">","s2")
elif (3*s1)<s2:
    print("s1","<","s2")
else:
    print("s1","=","s2")
