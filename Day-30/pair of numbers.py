n = int(input())
pair = 0
for i in range(1,n):
    if (n-i)< n and i < (n-i):
        pair = pair + 1
print(pair)    