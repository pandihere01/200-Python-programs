n = int(input())

for i in range(1,n+1):

    l_dot = ". "*(n-i)

    zero = "0 "*(2*i-1)

    h_space = 2*(". "*(n-i))

    print(l_dot + zero + h_space + zero + l_dot )