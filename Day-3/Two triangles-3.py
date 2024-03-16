n = int(input())
for i in range(1,n+1):
    if i == n:
        print(2*("* "*n))
    elif i == 1 or i == 2:
        print("* "*i +(2*("  "*(n-i))) + "* "*i) 
    else:
        print("* "+("  "*(i-2))+"* " +(2*("  "*(n-i)))+"* "+("  "*(i-2))+"* ")      