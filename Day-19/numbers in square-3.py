n = int(input())
num  =  1
for i in range(1,n+1):
    pattern = ""
    for j in range(1,n+1):
        pattern = pattern + str(num) +" "
        num = num + 1
    print(pattern)    