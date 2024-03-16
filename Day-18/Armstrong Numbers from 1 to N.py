n = int(input())
for i in range(1,n+1):
    sum = 0
    l = len(str(i))
    for digit in str(i):
        sum = sum + int(digit) ** l
    if sum == i:
        print(i)    


    