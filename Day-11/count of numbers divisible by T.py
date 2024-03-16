n = int(input())
t = int(input())
count = 0
for i in range(1,n+1):
    if i % t == 0:
        count = count +1
print(count) 

#n=12
#t=3