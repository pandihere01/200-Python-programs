x = int(input())
n = int(input())
sum = 0
power = 2
for i in range(1,n+1):
    term = x ** power
    power = power + 2
    sum = sum + term
print(sum)    

#x = 3
#n = 4