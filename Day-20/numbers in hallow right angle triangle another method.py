n = int(input())
for i in range(1,n+1):
    if i == 1 or i == 2 or i==n:
        p =""
        for j in range(1,i+1):
            p = p + str(j)+" "
        print(p) 
    else:
        print("1 "+ ("  "*(i-2))+ str(j))       