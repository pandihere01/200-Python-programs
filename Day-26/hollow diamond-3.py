n = int(input())

for i in range(1,n+1):

    star = "* "*(n-i+1)
    h_space = 2*("  "*(i-1))

    print(star + h_space + star)

for j in range(1,n+1):

    star = "* "*j

    h_space = 2*("  "*(n-j))

    print(star + h_space + star)