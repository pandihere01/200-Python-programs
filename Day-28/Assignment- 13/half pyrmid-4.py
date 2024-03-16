n = int(input())
k =int(input())
c = n - 1
for i in range(1,k+1):
    for j in range(i):
        c = c + 1
for i in range(1,k+1):
    result =""
    for j in range(i):
        result =  result + str(c)+" "
        c = c- 1
    print(result)           
# input- n = 10 and k = 5