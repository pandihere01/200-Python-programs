m = int(input())
n = int(input())
c = 1
for i in range(1,m+1):
    if i == 1 or i == m:
        p = ""
        for j in range(1,n+1):
            p = p + str(c )+" "
            c = c + 1
        print(p) 
    else:
        p = str(c)+" " 
        hollow_space = "  "*(n-2)
        c = c + int(len(hollow_space)/2)+1
        p = p + hollow_space + str(c)+" "
        c = c + 1
        print(p)         