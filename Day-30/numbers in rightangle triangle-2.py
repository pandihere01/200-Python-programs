n = int(input())
for i in range(1,n+1):
    left_space = "  "*(n-i)
    p =""
    for j in range(1,i+1):
        p = str(j)+" " + p
    print(left_space + p)    
