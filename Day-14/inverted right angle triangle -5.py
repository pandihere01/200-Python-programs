n  =int(input())
for i in range(n):
    left_space =("  "*i)
    pattern =((str(n-i)+" ")*(n-i))
    print(left_space + pattern)