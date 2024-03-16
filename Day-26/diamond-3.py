n = int(input())

for i in range(1,n+1):

    l_dot = ". "*(n-i)

    c_zero = "0 "*(i*2 - 1)

    print(l_dot + c_zero + l_dot)

for j in range(1,n):

    l_dot = ". "*(j)

    c_zero = "0 "*(2*(n-j)-1)

    print(l_dot + c_zero + l_dot) 