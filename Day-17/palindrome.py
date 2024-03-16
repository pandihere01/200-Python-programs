string = input()
s = ""
for i in string:
    s = i + s
if s == string:
    print("True-its a palindrome")
else:
    print("False- its not a palindrome")        