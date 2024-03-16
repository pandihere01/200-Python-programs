m = int(input())
n = int(input())
num = 1
for i in range(1,m+1):
    if i ==1 or i == m:
        a = ""
        for n in range(1,n+1):
            a = a + str(num)+" "
            num = num + 1
        print(a)
    else:
        a = str(num)+" "
        h_space = "  "*(n-2)
        num = num + int(len(h_space)/2)+ 1
        a = a + h_space + str(num) + " "
        num = num + 1
        print(a)          
