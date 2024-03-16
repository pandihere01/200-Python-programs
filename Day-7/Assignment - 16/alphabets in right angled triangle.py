n = int(input())
count = 0
c = 65
for i in range(1,n+1):
    left_space ="  "*(n-i)
    p =""
    for j in range(0,i):
        p = p + chr(c+j)+" "
    print(left_space + p)    