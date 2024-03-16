n = int(input())
prime_number = True
for i in range(2,n):
    if n % i == 0:
        prime_number = False
print(prime_number)        