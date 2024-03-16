n = int(input())

count_of_triplets = 0
for i in range(1,n):
    for j in range(i+1,n):
        if (n- (i+j)< n ) and (i<j<n - (i+j)):
            count_of_triplets = count_of_triplets + 1
print(count_of_triplets)            