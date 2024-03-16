n = int(input())
for i in range(n):
    s = ""
    for j in range(1,n-i+1):
        s = s + (str(j) + " ")
    print(s)    

