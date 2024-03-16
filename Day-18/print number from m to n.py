m = int(input())
n = int(input())
s =""
for i in range(m,n+1):
    if i > 1:
        factor = 0
    else:
        factor = 1
    for j in range(2,i):
        if i % j == 0:
            factor = factor + 1
    if factor == 0:
        s = s + str(i) + " "
if len(s) >= 1:
    print(s)
else:
    print("no prime number")                
