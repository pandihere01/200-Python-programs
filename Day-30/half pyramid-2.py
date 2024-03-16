n = int(input())
c = 1
for i in range(1,n+1):
    p =""
    for j in range(1,(i)+1):
        p = p + str(c)+" "
        c = c+1
    print(p)    