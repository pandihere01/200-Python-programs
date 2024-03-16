s = input()
p = ""
for i in s:
    if i.lower() == "a" or i.lower()=="e" or i.lower()=="i" or i.lower()=="o" or i.lower()=="u":
        continue
    else:
        p = p + str(i)
print(p)        