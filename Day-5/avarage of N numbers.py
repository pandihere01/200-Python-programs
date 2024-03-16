n = int(input())
sum = 0
count = 0
for i in range(1,n+1):
    sum = sum + i
    count = count + 1
    average = sum / count
print(average)
