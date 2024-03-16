n = int(input())
count = 0
for i in range(1,n):
    if (n-i) < n and (n-i) > i:
        print(i)


