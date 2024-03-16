n = int(input())
for i in range(1,n+1):
    left_space = " "*(n-i)
    star = "* "*i
    print(left_space + star)

for j in range(1,n):
    if j == n-1:
        left_space = " "*(j)
        star = "* "*1
        print(left_space + star)
    elif j == n-2:
        left_space = " "*j
        star = "* "*2
        print(left_space + star) 
    else:
        print((" "*j)+"* "+("  "*(n-j-2)) + "* ")     



