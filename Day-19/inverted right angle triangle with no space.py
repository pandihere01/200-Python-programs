n = int(input())
for row_num in range(0,n+1):
    p =""
    seq_num = n - row_num
    while seq_num > 0:
        p = p + str(seq_num)
        seq_num = seq_num -1
    print(p)    
