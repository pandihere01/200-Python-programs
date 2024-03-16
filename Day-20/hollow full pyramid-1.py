n = int(input())
for i in range(1,n+1):
    left_space = " "*(n-i)
    if i == 1 or i == 2 or i == n:
        print(left_space + "* "*i)
    else:
        h_space = "  "*(i-2)
        print(left_space +"* "+h_space +"* ")    
        