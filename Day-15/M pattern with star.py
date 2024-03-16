n = int(input())
for i in range(1,n+1):
    star = "* "*i
    center_space =  ("  ")*2 *(n-i)
    print(star + center_space + star)

# n = 6    