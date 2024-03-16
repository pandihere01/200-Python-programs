n = int(input())
for i in range(1,n+1):
    k =""
    for j in range(1,i+1):
        k = k + str(j) +" "

    for p in range(1,i):
        k = k + str(p)+" "
    print(k)      
