n = int(input())
for i in range(1,n+1):
    p =""
    c = 0
    left_space =(" "*(n-i))
    for j in range(1,i+1):
        p = p + str(j)+" "
        c = c + 1
    print(left_space + p)  

for i in range(1,n):
    left_space = (" "*i)
    p = ''
    for j in range(1,n-i+1):
        p = p + str(j)+" "
        c = c + 1
    print(left_space + p)    
