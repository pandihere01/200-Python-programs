n = int(input())
factor = 0
for i in range(2,n):
    if n%i == 0:
        factor = factor + 1
if factor >= 2:
    print("its a composite number")
else:
    print('its not a composite number')                