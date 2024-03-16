n = int(input())
for i in range(1,n+1):
    left_space =(" "*(n-i))
    star = "* "*i
    print(left_space + star)

for j in range(1,n):
    left_space = " "*j
    star = "* "*(n-j)
    print(left_space + star)    