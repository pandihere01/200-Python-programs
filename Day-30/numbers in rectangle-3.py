m = int(input())
n = int(input())
t = m * n
for i in range(1,m+1):
    p=""
    for j in range(1,n+1):
        p = p + str(t)+" "
        t = t - 1
    print(p)    