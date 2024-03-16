s_1 = "bring"
s_2 = "camel"
shuffle =""
for i in range(len(s_1)):
    if i % 2 == 0:
        shuffle = shuffle + s_1[i]
    else:
        shuffle = shuffle + s_2[i] 
print(shuffle)           
        