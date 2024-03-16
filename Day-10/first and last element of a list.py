n = int(input())

list_a = []

for i in range(n):
    list_a.append(int(input()))

list_b = [0,1,-2,-1]

result = []

for i in list_b:

    result.append(list_a[i])

print(result)