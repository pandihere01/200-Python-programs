n = int(input())
s = int(input())
last_no = n
for i in range(1,s+1):
    last_no = last_no + i
for j in range(1,s+1):
    r =""
    for k in range(j,s+1):
        if j == 1 or j == s-1 or j == s:
            r =  r + str(last_no - 1) +" "
            last_no = last_no - 1    
        else:
            if k == j or k == s:
                r =  r + str(last_no -1)+" "
                last_no = last_no - 1
            else:
                r = r + "  "
                last_no = last_no - 1
    print(("  "*(j-1))+ r)                    
             
