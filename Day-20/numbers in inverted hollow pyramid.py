n = int(input())
s = int(input())

t_r = ""
for i in range(n):
    t_r = t_r + str(s+i)+" "
print(t_r)

rightside_number = s+n-2
for j in range(1,n-1):
    left_space = j
    right_space = j
    middle_space = (2*n-1)-(left_space + right_space + 2)
    print(" "*left_space + str(s)+ " "*middle_space + str(rightside_number))
    rightside_number = rightside_number -1
print(" "*(n-1)+str(s))    
