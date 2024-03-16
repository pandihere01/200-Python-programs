string = input()
string = string.lower()
s=""
for i in string:
    s = i + s
if s == string:
    print("True")
else:
    print("False")      