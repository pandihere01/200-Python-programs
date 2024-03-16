n = int(input())
for i in range(1,n+1):
    left_space = " "*(n-i)
    if i == 1 or i == 2 or i == n:
        p =""
        for j in range(1,i+1):
            p =  "* "*j
        print(left_space+ p)
    else:
        middle_space = "  "*(i-2)
        print(left_space+'* '+ middle_space + "* ")        