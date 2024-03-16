n = int(input())
for i in range(1,n+1):
    star = "* "*i
    print(star)

for j in range(1,n):
    star = "* "*(n-j)
    print(star)    