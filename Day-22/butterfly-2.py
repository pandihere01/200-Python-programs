n = int(input())
for i in range(1,n+1):
    star = "* "*i
    hollow_space = 2*("  "*(n-i))
    print(star + hollow_space + star)

for j in range(n):
    star = "* "*(n-j)
    hollow_space_2 = 2*("  "*(j))
    print(star + hollow_space_2 + star)
