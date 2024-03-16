n = int(input())
for i in range(1,n+1):
    p =""
    if i == 1 or i == n:
        for j in range(1,n+1):
            p = p + str(j)+" "
    else:
        p = p + ("1 "+ ("  "*(n-2))+ str(n)) 
    print(p)     