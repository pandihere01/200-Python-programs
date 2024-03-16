n = int(input())

c = 65

for i in range(n):

    l_s = " "*(n-i-1)

    h_space = " "*(i*2 - 1)

    if i == 0:
        row = (l_s + chr(c))
        c = c +  1

    else:

        row = (l_s + chr(c)+h_space + chr(c))

        c += 1
    print(row)
c = c - 2

for j in range(1,n):

    l_s = " "*j

    h_space = " "*(2*(n-j-1)-1)

    if j == n-1:
        row = l_s + chr(c)

    else:

        row = l_s + chr(c)+h_space + chr(c)

        c = c  - 1

    print(row)        