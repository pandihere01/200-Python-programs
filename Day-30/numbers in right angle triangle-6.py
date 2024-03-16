n = int(input())
for i in range(1,n+1):
    p =""
    for j in range(1,i+1):
        p = p + str(j)+" "
    for k in range(1,i):
        p = p + str(k)+' '
    print(p)        