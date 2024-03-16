s_1 = input()
s_2 = input()
starts_with = s_1.startswith(s_2)
if starts_with:
    print("True")
elif s_1.endswith(s_2):
    print("True")
else:
    print("False")    