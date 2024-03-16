n = int(input())
c = 0
for i in range(1,n+1):
    if i % 2 != 0:
        print("* "*(i + c))
    else:
        print("* "*(i + c+ 1))   
        c = c + 2 
    
