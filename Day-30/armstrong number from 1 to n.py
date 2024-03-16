n = int(input())

for i in range(1,n+1):
    l = len(str(i))
    sum = 0
    for digit in str(i):
        sum = sum + int(digit) ** l
    if sum == i:
        print(i)      

    
