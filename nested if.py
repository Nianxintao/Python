# 2 statements - stat1 and state2 - take input from the user
state = input("Your state: ")
age = int(input("Your age: "))
if state == "VIC":
    if age >=18 :
        print("Yes you can vote!!!")
    else:
        print("No you can't vote!!!")
elif state == "NSW":
    if age >=20:
        print("Yes you can vote!!!")
    else:
        print("No You can't vote!!!")
elif state == "QLD":
    if age >= 22:
        print("Yes you can vote!!!")
    else:
        print("No you can't vote!!!")






