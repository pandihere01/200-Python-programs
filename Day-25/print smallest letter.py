s = input()

smallest_charecter = s[0]

for i in range(1,len(s)):

    if ord(s[i]) < ord(smallest_charecter):
        smallest_charecter = s[i]

print(smallest_charecter)        