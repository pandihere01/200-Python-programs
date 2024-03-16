m = int(input())
n = int(input())
for i in range(m,n+1):
    factor = 0

    for j in range(1,i+1):
        if i % j == 0:
            factor = factor + 1

    if factor == 2:
        print(i)
        break

if factor > 2:
    print("no prime number in the given range")        