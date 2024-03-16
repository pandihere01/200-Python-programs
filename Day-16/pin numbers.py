word = input()
digits =""
for i in word:
    if i.isdigit():
        digits = digits + i
if len(digits) == len(word):
    print("True")
else:
    print("False")    
    
             