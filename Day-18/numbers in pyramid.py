n = int(input())
s = int(input())
for i in range(1,n+1):
    left_space = " "*(n-i)
    p =""
    for j in range(s,i+s):
        p = p + str(j)+" "
    print(left_space + p)