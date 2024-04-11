login_attempts = 5
actual_passwd = "Hello"

while login_attempts > 0:
    passwd = input("Please enter your password: ")
    if passwd !=actual_passwd:
        print("wrong passwd")
        login_attempts -= 1
        print(f"Remaining attemps: {login_attempts}")
    else:
        print("Login successful")
        break
