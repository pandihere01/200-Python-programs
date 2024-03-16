n = int(input())
s = int(input())
for i in range(1,n+1):
    p =""
    for j in range(1,i*2+1):
        p = p + str(s) +' '
        s = s +1
    print(p)        
