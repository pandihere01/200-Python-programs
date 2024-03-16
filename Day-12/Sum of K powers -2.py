n = int(input())
sum =0
n = str(n)
length_n = len(n)
for i in n:
    sum = sum + int(i) ** length_n
print(sum)    
