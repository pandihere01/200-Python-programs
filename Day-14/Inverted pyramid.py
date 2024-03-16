n = int(input())
for i in range(n):
    left_space =" "*i
    star = "*"*(2*(n-i)-1)
    print(left_space + star)    