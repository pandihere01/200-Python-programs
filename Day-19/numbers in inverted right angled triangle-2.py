n = int(input())
first_number = 0
for i in range(1,n+1):
    first_number = first_number + i

for j in range(n):
    p = ""
    left_space = "  "*j

    for k in range(n-j):

        p = p + str(first_number) + " "
        first_number = first_number -1
    print(left_space + p)    