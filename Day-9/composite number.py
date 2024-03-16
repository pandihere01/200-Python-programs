n = int(12)
count = 0
for i in range(2,n):
    if n%i == 0:
        count = count + 1
        print(count)
if count >= 2:
    print("True")
else:
    print("False")            