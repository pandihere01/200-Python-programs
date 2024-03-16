m = int(input())
n = int(input())

if m > n:
    largest_number = m

else:
    largest_number = n

gcd = largest_number

for i in range(1,largest_number+1):
    if (m%i == 0) and (n%i == 0):
        gcd = i
print(gcd)        