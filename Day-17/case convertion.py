string = input()
s =""
for i in string:
    if i == i.upper():
        s = s + " "+ i
    else:
        s = s + i
print(s.strip()) 

#TheLionKing