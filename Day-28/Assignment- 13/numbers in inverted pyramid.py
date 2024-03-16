n = int(input())
s = 1
for i in range(n+1):
    p =""
    left_space =(" "*i)
    for j in range(1,n-i+1):
        p = p + str(j)+" "
        s = s + 1
    print(left_space + p)    
