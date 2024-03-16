n = int(input())
ascii_value = 65
for i in range(1,n+1):
    p =""
    for j in range(1,i+1):
        p = p + chr((ascii_value -1) + j)+" "
    print(p)        