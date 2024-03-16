m = int(input())
n = int(input())
p =""
for i in range(m,n+1):
    if i > 1:
        fact = 0
    else:
        fact = 1

    for num in range(2,i):
        if i% num == 0:
            fact = fact + 1
    if fact == 0:
        p = p + str(i)+' '
if len(p) >= 1:
    print(p)
else:
    print('no prime number found')            




