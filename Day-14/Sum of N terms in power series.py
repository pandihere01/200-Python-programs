n = int(input())
x = int(input())
p = 1
sum = 0
for i in range(1,n+1):
    term_x = x ** p
    p = p + 2
    sum = sum + term_x
print(sum)    

# x =2
# n = 6