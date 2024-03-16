num_list = [1,6,32,93,71,-20,30,-90,50]

n = int(input())

p =[]

for i in num_list:

    if i > n:

        p = p + [i]

print(p)        