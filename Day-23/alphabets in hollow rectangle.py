m = int(input())
n = int(input())
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
count = 0

for i in range(m):
    p = ""
    for j in range(n):
        if i == 0 or i == m-1:
            p = p + alphabets[count]+" "

        elif j == 0:
            p = p + alphabets[count]+" "*(2*n-3) +alphabets[n+count - 1] 

        count = count + 1

    print(p)                  
