n = int(input())
factor_count = 0
for i in range(2,n+1):
    if n % i == 0:
        factor_count = factor_count + 1
if factor_count >= 2:
    print("Number has more than two factors") 
else:
    print("Number doesn't have more than two factors")  

# note factor range can starts from 2 to n             