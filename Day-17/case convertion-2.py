s = input()
p =""
for i in s:
    if i == i.upper():
        p = p + "-" + i.lower()
    else:
        p = p + i
print(p)                

#aChristmasStory