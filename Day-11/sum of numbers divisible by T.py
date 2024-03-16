t = int(input())
m = int(input())
n = int(input())
sum = 0
for i in range(m,n+1):
    if i % t == 0:
        sum = sum  + i
print(sum)
#t=2
#m=5
#n=9

