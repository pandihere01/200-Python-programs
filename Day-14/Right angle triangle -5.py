a = int(input())
for i in range(1,a+1):
    left_space = "  "*(a-i)
    star ="*"*i
    print(left_space + star)