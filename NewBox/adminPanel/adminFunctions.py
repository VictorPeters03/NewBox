# Login function (without GUI for now)

print("***Register PIN****")
register_pin = input("Enter pin: ")

logged_in = False
failed_attempts = 0
max_attempts = 5

while not logged_in:
    if failed_attempts < max_attempts:
        print("***Login****")
        log_in_pin = input("Enter pin: ")
        if register_pin == log_in_pin:
            print("Login successful")
            logged_in = True
        else:
            failed_attempts = failed_attempts + 1
            print("False PIN")
    else:
        print("You have tried to log in too many times")
        break
