s = input().split()

first_word =s[0]

for i in s:

    if i.lower() < first_word.lower():
        first_word = i

print(first_word)        