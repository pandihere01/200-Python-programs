n = int(input())
n = str(n)
c = 0
for i in n:
    if int(i) == 0:
        c = c + 1
    else:
        continue
if c > 3:
    print("count of zero is greater than 3")
else:
    print("count of zero  is not greater than three")            

