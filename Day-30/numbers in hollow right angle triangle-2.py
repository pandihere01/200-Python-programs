n = int(input())
for i in range(1,n+1):
    left_space = "  "*(n-i)
    if i == 1 or i == 2 or i == n:
        p = ""
        for j in range(1,i+1):
            p = str(j)+" "+p
        print(left_space + p) 
    else:
        print(left_space + str(n-j+1)+" "+(("  "*(i-2)))+str(1))       