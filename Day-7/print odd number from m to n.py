m = int(input())
n = int(input())
s =""
for i in range(m,n+1):
    if i % 2 != 0:
        s = s + str(i) +" "
print(s)


