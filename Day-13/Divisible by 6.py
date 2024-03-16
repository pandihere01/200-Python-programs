m = int(input())
n = int(input())
s=""
for i in range(m,n+1):
    if i%6 ==0:
        s = s+str(i)+" "
if s:
    print(s)
else:
    print("No Numbers Found")            