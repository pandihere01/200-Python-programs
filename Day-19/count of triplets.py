n = int(input())

count = 0

for i in range(1,n):
    for j in range(i+1,n):
        if (n-(i+j)<n ) and (i<j<n - (i+j)):
            count = count + 1
print(count)     

#n = 10 -> (1,2,7)= 10, (1,3,6) = 10 ,(2,3,5)== 10 and (1,4,5)= 10