"""Sa se calculeze 1!+2!+3!+...+n! (n>1)"""
n=eval(input("dati un numar mai mare ca 1:"))
p=1
s=0
if n>1:
    for i in range(1,n+1):
        p*=i
        s+=p

else:
    print("n<=1")

print("suma=",s)