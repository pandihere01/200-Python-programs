n = int(input())
for i in range(1,n+1):
    p = ""
    left_space = " "*(n-i)
    for j in range(1,i+1):
        p = p + str(j)+" "
    print(left_space + p)   
    

