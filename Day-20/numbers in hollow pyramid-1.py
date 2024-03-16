n = int(input())
for i in range(1,n):
    left_space = n-i
    middle_space = (2*n-1) - ((2*left_space )+ 2)  
    if i==1:
        print(" "*left_space +"5") 
    else:
        print(" "*left_space + "5"+" "* middle_space+str(5+i-1))
last_row = ""
for j in range(n):
    last_row = last_row + str(5+ j)+' '
print(last_row)                 
