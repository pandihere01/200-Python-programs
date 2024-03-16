n = int(input())
print("+ "*n)
for i in range(1,n):
    if i == n-1:
        left_space ="  "*i
        print(left_space + "* "*(1))
    else:    
        print(("  "*i) + "* "+("  "*(n-i-2))+"* ")