m = int(12)
n = int(5)
for i in range(1,n+1):
    if i == 1:
        print("+"+("-"*(m-2))+"+")
    elif i == n:
        print("+"+("-"*(m-2))+"+")
    else:
        print(("|") + (" "*(m-2))+("|" ))  