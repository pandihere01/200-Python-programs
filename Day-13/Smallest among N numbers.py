n = int(input())
first_number = int(input())
smallest_number = first_number
for i in range(n-1):
    t = int(input())
    if smallest_number > t:
        smallest_number = t
print(smallest_number)        