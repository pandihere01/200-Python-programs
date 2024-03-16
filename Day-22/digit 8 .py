n = int(input())
k = (2 *n) + 1
for i in range(1,k+1):
    if i == 1 or i == n+1 or i == k:
        print("* "*n)   
    else:
        print("* "+("  "*(n-2))+"* ")             