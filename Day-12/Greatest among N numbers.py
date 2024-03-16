n = int(input())
first_number = int(input())
greatest_number = first_number
for i in range(n-1):
    t = int(input())
    if t > greatest_number:
        greatest_number = t
print(greatest_number)