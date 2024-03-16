n = int(input())
p = 1
for i in range(1,n+1):
    dot = ". "*(n-i)
    print(dot + "0 "*p + dot)
    p = p + 2
