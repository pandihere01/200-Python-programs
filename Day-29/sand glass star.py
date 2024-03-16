n = int(input())
for i in range(n):
    left_space = " "*(i)
    print(left_space + "* "*(n-i))

for j in range(2,n+1):
    left_space = " "*(n-j)
    print(left_space +"* "*(j))    