n = int(input())
for i in range(1,n+1):
    left_space = ("  "*(n-i))
    pattern = (str(i)+" ")*(2*i-1)
    print(left_space + pattern)