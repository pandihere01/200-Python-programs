n = int(input())
p = 1
for i in range(1,n+1):
 left_space = "  "*(n-i)
 pattern  = "1 "*i
 print(left_space + pattern)