n = int(input())
for i in range(1,n+1):
    if i == 1 or i ==n:
        print("* "*n)
    else:
        left_space ="  "*(n-1)
        print(left_space +"* ")  

for j in range(1,n):
    if j == n-1:
        print("* "*n) 
    else:
        print("* ")             