x = int(input())
n = int(input())
sum = 0
p = 0
for i in range(1,n+1):
    if i%2 == 0:
        p = p + 2
        term = -(x ** p)
    elif i%2 == 1:
        p = p + 2
        term = (x ** p)    
    sum = sum + term
print(sum)        

# x = 2
#n = 6
