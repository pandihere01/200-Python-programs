n = int(input())
sum_of_odd = 0
for i in range(1,n+1):
    if i % 2 == 1:
        sum_of_odd = sum_of_odd + i
print(sum_of_odd)        
