n = int(input())
p = 1
for i in range(1,n+1):
    d = ""
    for j in range(1, i + 1):
        d = d + str(p)+" "
        p = p + 1
    print(d)    


