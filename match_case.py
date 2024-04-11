# Match case - Switch Case
# 0- Monday
# 1-Tuesday
# 2-Wednesday
#  ...

day = int(input("chose a number: "))

match day:
    case 0:
        print("Monday")
    case 1:
        print("Tuesday")
    case 2 :
        print("Wednesday")
    case _:
        print("invalid Date")

