n = int(input())
s = int(input())
p = ""
for i in range(n):
    p = p + str(s+i)+" "
print(p)
   
right_side_digit = s + n - 2
for j in range(1,n-1):
    left_space = j
    right_space = j
    middle_space = 2*(n-1)- (left_space + right_space + 2)  
    print(" "*left_space + str(s)+" "+ " "*middle_space + str(right_side_digit))
    right_side_digit = right_side_digit - 1
print(" "*(n-1)+str(s) )   
