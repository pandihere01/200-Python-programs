n = int(input())

for i in range(1,n+1):
    if i == 1 or i == n:
        p = ""
        for j in range(1,n+1):
            p = str(j)+" "+p
        print(p) 
    else:
        middle_space = "  "*(n-2)
        print(str(n)+" "+ middle_space + str(1))       
