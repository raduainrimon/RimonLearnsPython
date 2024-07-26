#weight = input("Weight: ")
weight = float(input("Weight: "))
unit = input("(L)bs or (K)g: ")
#1kg = 2.2 pound
#if (unit=='l' or unit == 'L'):
if unit.upper()=="L":
    pk=weight/2.2
    #print(pk)
    print(f"you are {pk} kilos")
#elif (unit=='k' or unit=='K'):
elif unit.upper() == "K":
    kp=weight*2.2
    #print(kp)
    print(f"you are {kp} pounds")
else:
    print("Type (k/K/l/L)")