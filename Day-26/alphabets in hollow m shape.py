n = int(input())

c = 65

for i in range(n):

    l_s = " "*(n-i)

    ins_space = " "*(i*2-1)

    h_space = 2*(" "*(n-i))

    if i == 0:

        print(l_s + chr(c)+ h_space + chr(c))

        c = c + 1

    else:

        print(l_s + chr(c)+ins_space + chr(c)+ h_space + chr(c)+ins_space + chr(c))
        c = c + 1    