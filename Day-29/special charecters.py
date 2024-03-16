s = input()
p =""
d =""
vowels_count = 0
consonent_count = 0
for i in s:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        p = p + str(i)
        vowels_count = vowels_count +1 
    elif i == " ":
        continue    
    else:
        d = d + str(i)
        consonent_count = consonent_count + 1
print(vowels_count)        
print(consonent_count)