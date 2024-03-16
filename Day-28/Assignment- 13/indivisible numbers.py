n = int(input())
count = 0
for i in range(1,n+1):
    if (i%2 != 0) &(i%3 != 0) &(i%4 != 0) &(i%5 != 0) &(i%6 != 0) &(i%7 != 0) &(i%8 != 0) &(i%9 != 0) &(i% 10 != 0):
        count = count + 1
print(count)      