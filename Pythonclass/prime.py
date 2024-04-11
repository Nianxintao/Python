#  if a number a prime or not

number = int(input("enter a number: "))

for i in range (2, number):
    if number % i == 0:
        print("Not a prime number")
        break
    else:
        print("A prime number")