n = input().split()

sum_of_numbers = 0

count = 0

for i in n:

    sum_of_numbers = sum_of_numbers + int(i)

    count = count + 1

    average = sum_of_numbers /  count

print(round(average,2))    