s = input()
p = ""
c = 0
for i in s:
    if i.isupper():
        if c==0:
            p = p +i.lower()
            c = c + 1
        else:
            p = p + "-" + i.lower()
    else:
        p = p + i        
print(p)            


#TitleCase  to title-case it will print