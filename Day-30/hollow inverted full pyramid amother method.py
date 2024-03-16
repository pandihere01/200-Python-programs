n = int(input())
for i in range(n):
    left_space = " "*i
    r = n - i
    if r == 1 or r == 2 or r == n:
        p  =""
        for j in range(1,r+1):
            p = p + str(j)+" "
        print(left_space + p) 
    else:
        hollow_space = "  " *(r-2)
        print(left_space + str(1)+" "+ hollow_space + str(r))      