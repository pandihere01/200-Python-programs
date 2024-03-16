m = int(input())
n = int(input())
s=""
for i in range(m,n+1):
    if i%2 != 0:
        s = str(i)+" "+s
print(s)   

#m=1
#n=10