m = int(input())
n = int(input())
num = ""
for i in range(n):
    num = num + str(7+ i) +" "

for j in range(m):
    if j == 0 or j ==m-1:
        print(num)    

    else:
        print(str(7)+" "+(("  "*(n-2)))+str(7+n-1))    
       
        


