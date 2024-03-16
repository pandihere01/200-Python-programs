s = input()
for i in s:
    if i.isdigit():
        continue
    elif i == i.upper():
        break
print(i)    