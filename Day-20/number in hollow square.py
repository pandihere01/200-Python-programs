n = int(input())
p = ""
for i in range(1,n+1):
    p = p + str(i)+" "
for i in range(1,n+1):
    if i == 1 or i == n:
        print(p)
    else:
        print("1 "+("  "*(n-2))+str(n))    
                