m = int(input())
n = int(input())
num = ""
for i in range(m):
    num = num + str(7+i) +" "

for j in range(n):
    if j== 0 or j == n-1:
        print(num)
    else:
        print(str(7)+" "+(("  "*(m-2))+str(7+m-1)))
    