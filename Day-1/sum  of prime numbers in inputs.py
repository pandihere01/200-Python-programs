n = int(input())
sum  = 0
for i in range(n):
    t = int(input())
    f = 0
    for j in range(1,t):
        if t % j == 0:
            f = f + 1
    if f == 1:
        sum = sum + t
print(sum)                
