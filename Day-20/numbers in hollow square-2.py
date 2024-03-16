n = int(input())
for i in range(n):
    p =""
    for j in range(n):
        p = p + str(n-j)+' '
    if i == 0 or i == n -1:
        print(p)
    else:
        print(str(n)+" " +("  "*(n-2))+"1 ")    

