n = int(input())
count = 1
for i in range(1,n+1):
    h_space = "  "*(n-i-1)
    if i == 1 or i ==n:
        result = ""
        for j in range(n-i+1):
            result = result + str(count)+' '
            count += 1
        print(result) 
    else:
        print(str(count)+" "+ h_space +str(count+(n-i)))


