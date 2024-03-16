m = int(input())
n = int(input())
if m > n:
    greatest_number = m

else:
    greatest_number = n

lcm_found = False
for i in range(greatest_number,(m*n+1)):
    if not lcm_found:
        if ((i%m)== 0 and (i%n == 0)):
            lcm_found = True
            lcm = i

print(lcm)                    