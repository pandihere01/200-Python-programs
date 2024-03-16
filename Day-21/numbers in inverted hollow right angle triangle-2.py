n = int(input())
s = int(input())
for i in range(1,n+1):
    result = ""
    if i == 1:
        for j in range(n):
            result = result + str(s) +" "
            s = s + 1
    elif i == n:
        left_space = "  "*(n-1)
        result = left_space + str(s)         
    else:
        left_space = "  "*(i-1)
        holow_space = "  "*(n-i-1)
        result = left_space + str(s)+" "+ holow_space + str(s+1)
        s = s + 2
    print(result)        