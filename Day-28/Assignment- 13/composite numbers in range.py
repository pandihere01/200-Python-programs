m = int(input())
n = int(input())
factor = 0
for i in range(m,n+1):
    for j in range(2,i):
        if i % j == 0:
            print(i)
            break         