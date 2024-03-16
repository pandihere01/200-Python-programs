n = int(input())
for i in range(1,n+1):
    star = "* "*i
    center_space = ("  "*(2*n - 2 *i))
    print(star + center_space + star)
for j in range(1,n):
    star = "* "*(n-j)
    space = "  "*(2*j)
    print(star + space + star)