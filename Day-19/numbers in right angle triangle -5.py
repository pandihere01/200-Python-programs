n = int(input())
s = int(input())
first_number = s
for i in range(1,n+1):
    first_number = first_number + i
first_number = first_number - 1    

for i in range(1,n+1):
    p = ""
    for j in range(i):
        p = p + str(first_number)+" "
        first_number = first_number - 1
    print(p)
