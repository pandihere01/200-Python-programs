n = int(7)
m = int(5)
for i in range(1,m+1):
    space =(" "*(m-i))
    num =""
    for j in range(n,i + n):
        num = num + str(j) +" "
    print(space + num)    