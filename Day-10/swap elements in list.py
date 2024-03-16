L = [1,"two",9,5.09, "Three",-558,"four",-93.6,"six"]

first = int(input())

second = int(input())

r = []

for i in range(len(L)):

    if i == first:

        r.append(L[second])


    elif i == second:

        r.append(L[first])
    
    else:

        r.append(L[i])
print(r)