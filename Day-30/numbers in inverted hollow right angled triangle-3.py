n = int(input())
count = 0
for i in range(1,n+1):
    count = count + i

for i in range(1,n+1):
    result = ""
    if i == 1 :
        for r  in range(n):
            result =  result + str(count)+" "
            count = count -1 
    
    elif i == n:
        result = ("1")  
    else:
        hollow_space = "  "*(n-i-1)
        result = result +  str(count)+" "+ hollow_space + str(count-(n-i))
        count = count - (n-i+1)
    print(result)           