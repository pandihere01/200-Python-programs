n = int(input())
k = int(input())

factor = n
kth_factor = 0
for i in range(1,n+1):
    if n % factor == 0:
        kth_factor = kth_factor + 1
        if kth_factor == k:
            break
    factor = factor - 1

if factor <= 0:
    print("1")
else:
    print(factor)            