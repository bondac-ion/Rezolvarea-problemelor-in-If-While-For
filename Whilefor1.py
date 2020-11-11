"""se da numarul n apartine (28,29,30,31) sa se afiseze lunile cu numarul n de zile"""
n=int(input("dati un numar:"))
if(n==28):
    print("Februarie")
elif(n==29):
    print("Februarie în an bisect")
elif(n==30):
    print("Aprilie, iunie, septembrie, noiembrie")
elif(n==31):
    print("Ianuarie, martie, mai, iulie, august, octombrie, decembrie")
else:
    print("Error")