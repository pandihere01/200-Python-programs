s = input()

for i in s:

    if i ==" ":
        continue
    else:
        prev = ord(i)-1
        print(chr(prev))