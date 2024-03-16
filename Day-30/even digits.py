n = int(input())
count = 0
for i in range(1,n+1):
    if i % 2 == 0:
        count = count + 1
    else:
        continue
if count > 2:
    print('count of even digits is greater than two')
else:
    print("count of even digits is not greater than 2")            
