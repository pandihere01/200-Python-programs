m = int(input())
n = int(input())
starting_number = m * n
for i in range(m):
    p =""
    for j in range(n):
        p = p + str(starting_number)+" "
        starting_number = starting_number - 1
    print(p)    