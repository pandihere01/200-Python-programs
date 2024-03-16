n = int(input())
for i in range(n):
    t = int(input())
    factor = 0
    for j in range(1,(t//2)+1):
        if t%j == 0:
            factor = factor + 1
    if factor == 1:
        print(t)
        break        
