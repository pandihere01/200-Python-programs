password = input()

valid = False
for i in password:
    if i.isalpha():
        valid = True
    elif i.isdigit():
        valid = True
if valid:
    print("Valid password")
else:
    print("not a valid password")     

# qwerty00               