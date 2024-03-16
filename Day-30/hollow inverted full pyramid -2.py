n = int(input())
p = ""
for i in range(1,n+1):
    p = p + str(i)+" "
print(p) 

right_side_digit = n-1
for j in range(1,n-1):
    left_space = j
    right_space = j
    center_space = ((2*n-2)-(left_space+right_space + 2))
    print(" "*left_space + str(1)+" "+ " "*center_space + str(right_side_digit))
    right_side_digit = right_side_digit -1
print(" "*(n-1)+str(1))    