s = input()

n = int(input())

count = 0

for i in s:
    if int(ord(i)) == n:
        count = count + 1

print(count)        
