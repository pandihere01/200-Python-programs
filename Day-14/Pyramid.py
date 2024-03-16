p = int(input())
for i in range(p+1):
    left_space = "  "*(p-i)
    star = ("* "*(2*i - 1))
    print(left_space + star)
