x = int(input())
n = int(input())
sum = 0
p = 1
for i in range(1,n+1):
    if i % 2 == 0:
        term = -(x ** p)
        p = p + 2

    elif i % 2 == 1:
        term = (x ** p)
        p = p + 2
    sum = sum + term
print(sum)        
 
# x = 2
# n = 5 