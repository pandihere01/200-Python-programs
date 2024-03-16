n = int(input())
for i in range(n):
    left_space = " "*i
    star =("* "*(n-i))
    center_space = "  "*(i)
    print(left_space + star + center_space + star)