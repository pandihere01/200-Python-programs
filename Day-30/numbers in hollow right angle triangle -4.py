n = int(input())
s = int(input())
l_n = n
for i in range(1,s+1):
    l_n = l_n + i

for j in range(1,s+1):
    r = ""
    for k in range(j,s+1):
        if j == 1 or j == s-1 or j == s:
            r = r + str(l_n - 1)+" "
            l_n = l_n - 1

        else:
            if k == j or k == s:
                r = r + str(l_n - 1)+" "
                l_n = l_n - 1

            else:
                r = r +"  "
                l_n = l_n - 1
    print(("  "*(j-1))+ r)            





















           



            

   

