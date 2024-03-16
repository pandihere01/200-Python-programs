n = int(input())
sum = 0
for i in range(1,n+1):
    two_series = "2"*i
    sum = sum + int(two_series)
print(sum)    