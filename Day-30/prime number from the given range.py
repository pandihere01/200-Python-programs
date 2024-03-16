m = int(input())
n = int(input())
for i in range(m,n+1):
    factor_count = 0
    for j in range(1,i+1):
        if i % j == 0:
            factor_count = factor_count + 1   

    if factor_count == 2:
        print(i)
        break
if factor_count > 2:
    print("No prime numbers in the given range")        