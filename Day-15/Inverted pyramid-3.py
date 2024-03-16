n = int(input())
print("+ "*n)
for i in range(1,n):
    left_space = " "*(i)
    star = "* "*(n-i)
    print(left_space + star)


    