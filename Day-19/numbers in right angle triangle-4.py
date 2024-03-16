n = int(input())
s = int(input())
for i in range(1,n+1):
    d= ""
    for j in range(i * 2):
        d = d + str(s) +" "
        s = s + 1
    print(d)    
