s = input()
h = ""
for p in s:
    i= p.lower()
    if i =="a" or i=="e" or i=="i" or i=="o" or i=="u":
        h = h +""
    else:
        h = h + p
print(h)            

