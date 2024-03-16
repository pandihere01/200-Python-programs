s = input()
space = 0
for i in s:
    if i == " ":
        break
    space = space + 1

upper_case = s[:space].upper() 
new_sentence = upper_case + s[space:]  
print(new_sentence)