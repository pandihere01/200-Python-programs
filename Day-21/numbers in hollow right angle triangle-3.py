s = int(input())
n = int(input())

for i in range(1,n+1):
    result = ""

    if i==1:
        result =  str(s)
        s = s + 1
    elif i == n:
        for j in range(n):
            result = result + str(s)+" "
            s += 1
    else:
        h_space = "  "*(i-2) 
        result = str(s)+" "+ h_space + str(s+1)
        s = s + 2
    print(result)                
