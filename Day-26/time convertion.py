t = input()

if t[-1] == "M":

    hour = int(t[:-1])/60

    print(str(round(hour,2))+"H ")

elif t[-1] == "S":

    hour = int(t[:-1])/3600 
    print(str(round(hour,2))+"H ")
     