n = int(input())

n_list = input().split()

for i in range(n):

    n_list[i] = int(n_list[i])

print(n_list[ : (n+1) // 2  ])    

