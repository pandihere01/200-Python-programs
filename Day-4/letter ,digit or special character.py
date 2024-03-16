c = input()

if c.isdigit():
    print("Digit")

elif c != c.upper():
    print("lowercase")

elif c != c.lower():
    print("uppercase")

else:
    print("special charecter")    