"""Mihai are un unchi bogat care i-a daruit in ziua cind s-a nascut un dolar, iar in fiecare an el dubla cadoul  si mai adauga atitia dolari
citi ani implinea mihai.
a)sa se calculeze citi dolari a primit Mihai atunci cind a implinit n ani(n<20).
b)La ce virsta cadoull lui Mihai era mai mare de 100$?"""
n=eval(input("dati un numar mai mic ac 20:"))
c=1
a=0
for i in range(1,n+1):
    c=c*2+i
       
print("La",n,"ani","Mihai a primit",c,"dolari")

c=1
for i in range(1,20):
    while c<=100:
        c=c*2+i
        a+=1

print("La virsta de",a,"ani va primi mai mult de 100$")
    