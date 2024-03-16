m = int(input())
n = int(input())
a = ""
for i in range(1,m+1):
    if i%2 == 1:
        print("* "*n)
    elif i%2 == 0:
        print("- "*n)
