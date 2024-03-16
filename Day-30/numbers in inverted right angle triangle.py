n = int(input())
for i in range(n):
    pattern = ""
    for j in range(1,(n-i)+1):
        pattern  = pattern + str(j)+" "
    print(pattern)    

