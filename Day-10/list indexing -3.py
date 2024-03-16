n = int(input())

t = int(input())

n_list = []

t_list = []

for i in range(n):

    n_list.append(int(input()))

for i in range(t):
    t_list.append(int(input()))

for i in t_list:

    print(n_list[i])        