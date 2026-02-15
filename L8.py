# s=int(input("primul numar "))
# n=int(input("al doilea numar "))
# for i in range(1,n):
#     if (i%2==0):
#         a=a-i*i
#     else:
#         a=a+i*i
# print(a)
n=int(input("indrodu un numar "))
s=0
for i in range(1,n+1):
    if(i%3==1 and i<5):
        s=s+i-4
    else:
        s=s+1
print(s)