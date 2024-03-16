w = input()
a = False
if w == w.lower():
    a = False
elif w == w.upper():
    a = False
else:
    for i in w :
        digit = i.isdigit()
        if digit:
            a = True
        else:
            a = True
if a:
    print("valid password")
else:
    print("invalid password")     

#Qwerty00 contains one lower charecter one digit and one uppercase                           