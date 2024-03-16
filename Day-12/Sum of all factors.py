n = int(input())
sum= 0
for i in range(1,n+1):
    if n%i == 0:
        sum = sum +i

print(sum)

# factors are 1+ 2+ 3+ 6 = 12 