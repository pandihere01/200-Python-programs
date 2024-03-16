word = input()
s =""
c = 0
for i in word:
    if i.isupper():
        if c == 0:
            s = s + i.lower()
            c = c + 1
        else:
            s = s + "-"+i.lower() 
    else:
        s = s + i
print(s)                       