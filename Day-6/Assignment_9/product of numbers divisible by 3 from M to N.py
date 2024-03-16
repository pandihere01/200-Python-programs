m = int(input())
n = int(input())
product = 1
for i in range(m,n+1):
    if i%3 ==0:
        product = product * i
print(product)        

#m =2
#n =7