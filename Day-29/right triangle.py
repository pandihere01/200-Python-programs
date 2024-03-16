n = int(input())
for i in range(1,n+1):
    e_space =""
    for j in range(1,i+1):
        e_space = e_space + str(j)
    for k in range(i-1,0,-1):
        e_space = e_space + str(k)
    print(e_space)     
