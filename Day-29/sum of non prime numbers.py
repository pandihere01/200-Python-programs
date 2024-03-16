n = int(input())
sum= 0
for i in range(n):
    factor = 0
    t = int(input())
    for j in range(2,n):
        if t % j == 0:
            factor = factor + 1
            break
    if factor != 0:
        sum = sum + t
print(t)            
