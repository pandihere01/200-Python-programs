n = int(input())
for i in range(1,n+1):
    p = ""
    if i == 1:
        left_space = " "*(n-1)
        print(left_space + "1")
    else:
        left_space = " "*(n-i)
        hollow_space = "  "*(i-2) 
        print(left_space + str(1)+" "+ hollow_space+ str(i))

for j in range(1,n):
    if j == n-1:
        print(" "*(n-1)+str(1))

    else:
        left_space = " "*j
        hollow_space = "  "*(n-j-2)  
        print(left_space + str(1)+" "+ hollow_space + str(n-j))  
