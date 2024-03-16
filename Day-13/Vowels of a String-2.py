string = input()
count = 0
for i in string:
    if i=='a' or i=="e" or i=='i' or i=='o' or i=="u":
        count = count + 1
if count > 2:
    print("String has more than two vowels")  
else:
    print("String doesn't have more than two vowels")          