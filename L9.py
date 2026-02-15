# citescte de la tastatura un numar N
# acesta numar cara il vei pune la tastura reprezinta cate numere vei introduce
# la final. progamul trebuie sa afisese cel mai mare numar dinte cele introduse
# ex: n=5. x1=2,x2=4,x3=0,x4=50
# x=int(input("intodu N numere "))
# max=int(input("Da-mi numarul 1 "))
# for i in range (2,x+1):
#     number=int(input(f"Da-mi numarul {i} "))
#     if number>max:
#         max=number
# print(f"maxinmul este: {max}")

# citescte de la tastatura un numar N
# acesta numar cara il vei pune la tastura reprezinta cate numere vei introduce
# afiseaza. cate numere sunt pare si mai mai mari decat zece.
# cate numere sunt impare si mai mici decat zece si suma tuturor numerelor

# x=int(input("intodu N numere "))
# suma=0
# par=0
# impar=0
# for i in range (1,x+1):
#     number=int(input(f"Da-mi numarul {i} "))
#     suma+=number  #suma=suma+number
#     if number%2==0 and number>10:
#         par+=1
#     if number%2==1 and number<10:
#         impar+=1 
# print(f"numerele impare sunt: {impar}")
# print(f"numerele par sunt: {par}")
# print(f"suma totala este: {suma}")

# citeste un numar N
# afiseas toate numerele de la 1 la N cara sunt divizibile cu 3 si 5
x=int(input("da-mi un numar "))
for i in range(1,x+1):
    if i%5==0 and i%3==0:
        print(i)