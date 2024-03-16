n = int(input())
c = 65
for i in range(n):
    p =""
    for j in range(n-i):
        p = p + chr(j+c)+" "
    print(p)    