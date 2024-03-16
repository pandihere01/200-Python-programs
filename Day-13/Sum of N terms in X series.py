x = int(input())
n = int(input())
sum = 0
for i in range(1,n+1):
    term = str(x)*i
    sum = sum + int(term)
print(sum)    
