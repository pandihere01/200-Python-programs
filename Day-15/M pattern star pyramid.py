n = int(input())
for i in range(1,n+1):
    left_space =" "*(n-i)
    star = "* "*i
    center_space = " "*2*(n-i)
    print(left_space + star + center_space + star)
