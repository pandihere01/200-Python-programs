m = int(input())
n = int(input())
p = 1
for i in range(m):
    pattern = ""
    for j in range(n):
        pattern = pattern + (str(p) + " ")
        p = p + 1
    print(pattern)    
