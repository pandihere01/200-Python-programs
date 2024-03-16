n = int(input())
s = int(input())
first_num = s
for i in range(1,n+1):
    first_num = first_num + i
first_num = first_num - 1
    
for j in range(1,n+1):
    p =""
    for l in range(j):

        p = p + str(first_num)+" "
        first_num = first_num -1
    print(p)    
    


