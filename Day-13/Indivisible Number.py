n = int(input())
count =0
for i in range(2,9+1):
    if n%i == 0:
        count = count + 1
if count == 0:
    print('Indivisible Number')
else:
    print("Divisible Number")    