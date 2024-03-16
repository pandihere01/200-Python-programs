m = int(input())
n = int(input())

for i in range(m,n+1):
    factor = 0
    for j in range(2,i):
        if i % j == 0:
            factor = factor + 1
    if factor == 0:
        print(i)        
  