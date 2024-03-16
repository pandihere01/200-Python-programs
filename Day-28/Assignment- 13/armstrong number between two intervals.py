a = int(input())
b = int(input())
x = ""
for i in range(a,b+1):
    length = len(str(i))
    i = str(i)
    sum_of = 0
    z = 0
    while z < length:
        sum_of = sum_of + (int(i[z]))** length
        z = z + 1
    if sum_of == int(i):
        x = x + str(sum_of)+" "
if x=="":
    print(-1)
else:
    print(x)                
# a= 120 
# b = 200
#in these two intervals armstorng number has been calculated
