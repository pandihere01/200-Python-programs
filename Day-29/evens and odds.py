m = int(input())
n = int(input())
even_count = 0
odd_count = 0
for i in range(m,n+1):
    if i % 2 == 0:
        even_count = even_count + 1
    elif i % 2 == 1:
        odd_count = odd_count + 1
print(even_count) 
print(odd_count)           
