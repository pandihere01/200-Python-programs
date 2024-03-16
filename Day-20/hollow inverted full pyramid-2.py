n = int(input())
for i in range(n):
    left_space = " "*i
    k = n-i
    if k == 1 or k == 2 or k == n:
        num = ""
        for j in range(1,k+1):
            num = num + str(j)+' '
        print(left_space+num)
    else:
        h_space = "  "*(k-2)
        print(left_space + "1 "+h_space+str(k))   
