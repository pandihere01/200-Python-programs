n = int(input())
count = 0
for i in str(n):
    if int(i) == 0:
        count = count + 1
    else:
        continue
if count > 2:
    print("count of zero is more than three ") 
else:
    print("count of zero is not more than three")  



#n=10203400