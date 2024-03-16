n = int(input())
for i in range(1,n+1):
    p =""
    for j in range(1,i+1):
        p = p + str(j) +" "
    if j == 1 :
        print(j) 
    elif j == n:
        print(p)   
    else:
        print("1 "+ (("  "*(j-2))+ str(j)))    
    