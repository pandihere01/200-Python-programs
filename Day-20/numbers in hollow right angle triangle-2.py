n = int(input())
for i in range(1,n+1):
    if i == n:
        p =""
        for j in range(n):
            p = p + str(n-j)+" "
        print(p)
    elif i == 1:
        print((" "*(2*n-2)+"1 "))
    else:
        space = " "*(2*(n-i)) 
        hollow_space = "  "*(i-2)  
        result = space + (str(i)+' ') + hollow_space + "1"
        print(result)        
