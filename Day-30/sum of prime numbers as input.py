n = int(input())
sum = 0
for i in range(n):
    t = int(input())
    factor = 0
    for j in range(1,t):
        if t % j == 0:
            factor = factor + 1

    if factor == 1:
        sum = sum + t

print(sum)             
