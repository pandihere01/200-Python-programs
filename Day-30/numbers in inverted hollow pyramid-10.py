n = int(input())
s = int(input())

add_num = n
for  i in range(1,s+1):
    r = ""
    for j in range(i,s+1):
        if i == 1 or i == s or i== s-1:
            r = r + str(add_num) +" "
            add_num = add_num + 1

        else:
            if j == i or j == s:
                r= r + str(add_num) +" "
                add_num = add_num + 1
            else:
                r = r + "  "
                add_num  = add_num + 1

print((" "*(i-1))+ r)                    
                  
