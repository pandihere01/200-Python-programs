n = int(input())
count = 1
for i in range(1,n+1):
    hollow_space = "  "*(n-i-1)
    if i == 1 or i == n:
        p = ""
        for j in range(n-i+1):
            p = p + str(count)+" "
            count = count + 1
        print(p)    
    else:
        print(str(count)+" "+hollow_space + str(count+(n-i)))
        count = count + (n-i+1)
        