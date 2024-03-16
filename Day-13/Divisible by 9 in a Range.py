m = int(input())
n = int(input())
count =0
s=""
for i in range(m,n+1):
    if i%9 == 0:
        count = count +1
        s = s+str(i)+" "
if count > 0:
    print(s)
else:
    print("No number Found")            