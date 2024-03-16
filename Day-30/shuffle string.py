string_1 = input()
string_2 = input()
result = ""
for i in range(len(string_1)):
    if i%2 == 0:
        result = result + string_1[i]
    elif i % 2 ==1:
        result = result + string_2[i]
print(result)            