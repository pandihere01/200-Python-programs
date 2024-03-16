n = int(input())
for i in range(1,n+1):
    left_space =(" "*(n-i))
    pattern = (str(i)+" ")*(i)
    print(left_space + pattern)