url = input()
secured_url = url.startswith("https://")
if secured_url:
    print("True")
else:
    print("False")    
