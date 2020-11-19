"""De aflat daca numarul n introdus de la tastatura este perfect(este egal cu suma divizorilor sai )"""
n=int(input("Dati un numar:"))
s=0
for i in range(1,n):
    if n%i==0:
        s+=i
print(s)       
if s==n:
    print("Este numar perfect")
else:
    print("Nu este numar perfect")