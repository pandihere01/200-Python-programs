a = input()
a = a.lower()
rev_word = ""
for i in a:
    rev_word = i + rev_word
if rev_word == a:
    print("palindrome")
else:
    print("not a palindrome")        
