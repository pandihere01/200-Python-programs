n = int(input())
s = int(input())
for  i in range(1,n+1):
    p = ""
    if i == 1:
        for j in range(1,i+1):
            p =  str(s)+" "
            s = s + 1
    elif i == n:
        for j in range(n):
            p = p + str(s)+" "
            s = s + 1
    else:
        hollow_space = "  "*(i-2)
        p =  str(s)+" "+  hollow_space + str(s+1)
        s = s + 2
    print(p)          
