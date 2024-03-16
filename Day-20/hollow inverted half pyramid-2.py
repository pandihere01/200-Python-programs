n = int(input())
for i in range(1,n+1):
    k = n+1-i
    if k == 1 or k == 2 or k ==n:
        pattern = ""
        for j in range(1,k+1):
            pattern = pattern + str(j) +" "
        print(pattern)
    else:
        h_space = "  "*(k-2)
        print("1 "+h_space + str(k))        