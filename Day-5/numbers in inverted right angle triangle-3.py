n = int(input())
s = int(input())
sum = 0
for i in range(1,n+1):
    sum = sum + i
k = sum
z = k + s -1
c = 0
for i in range(n):
    p = ""
    for j in range(n-i):
        p = p + str(z-c) +" "
        c = c + 1
    print(p)          