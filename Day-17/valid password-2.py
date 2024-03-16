word = input()
valid = False
if word == word.lower():
    valid = False
else:
    for i in word:
        digit = i.isdigit()
        if digit:
            valid = True
        else:
            valid = True
                
if valid:
    print("Valid password")
else:
    print("invalid password")                    