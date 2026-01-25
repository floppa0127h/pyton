# afiseaza toate numerele impare divizibile cu trei pornind dela 49 la 301 
# aceste doua valori sunt introduse de la tastatura
# for i in range(1,1001):
#     print("hello")
# a=int(input("introdu prima variabila "))
# b=int(input("introdu a doua variabila "))
# for i in range (a,b+1):
#     if (i%2==1 and i%3==0):
#         print(i)
# screiesti toate numereele pare pana la 100 la 24 inclusiv 24 si 100 
# a=int(input("introdu prima variabila "))
# b=int(input("introdu a doua variabila"))
# for i in range (a,b+1,2):
#     print (i)
a=int(input("introdu prima varibila "))
b=int(input("indrodu prima varibile "))
if (a<b):
    aux=a
    a=b
    b=aux
for x in range (a,b,-1):
    if x%2!=0:
        print(x)