n = int(input())
for i in range(1,n+1):
    if i%2 == 0:
        star = "* "*i
        left_space = " "*(n-i)
        print(left_space + star)