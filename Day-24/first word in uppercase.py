s = input()
space = 0
for i in s:
    if i == ' ':
        break
    space = space + 1

upper_word = s[:space].upper()

new_sentence = upper_word + s[space:]
print(new_sentence)

