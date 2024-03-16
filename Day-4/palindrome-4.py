s = input()
s = s.lower()
p = ""
for i in s:
    if i != " " and i !="'":
        p = i + p 
print(p == p[::-1])        

#No lemon no melon