s = input()

s_c = s[0].lower()

for i in s[1:]:
    if i in s.upper():
        s_c = s_c + "_"
        s_c = s_c + (i.lower())
    else:
        s_c = s_c + i
print(s_c)        