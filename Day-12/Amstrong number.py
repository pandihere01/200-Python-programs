n = int(input())
n = str(n)
length_n = len(n)
sum = 0
for i in n:
    sum = sum + (int(i)**length_n) 
if sum == int(n):
    print("Armstrong Number")
else:
    print("Its not an Armstrong number")      