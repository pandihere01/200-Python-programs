n = int(input())
k = int(input())

count = 0
for i in range(n):
    if n % (n-i) == 0:
        count = count + 1
        if count == k:
            print(n-i)