import string
from flaskApp import create_app

# ***** PASSWORD FUNCTIONS *****

# Password register check

app = create_app()

if __name__ == '__HtmlPlaceholder__':
    app.run(debug = True)


def click():
    caps = string.ascii_uppercase
    numbers = []
    for i in range(10):
        numbers.append(str(i))
    special_chars = ['!', '@', '#', '$']
    registered = False

    def number_found(pw):
        found = False
        for number in numbers:
            if pw.find(number) > -1:
                found = True
        return found

    def caps_found(pw):
        found = False
        for letter in caps:
            if pw.find(letter) > -1:
                found = True
        return found

    def special_found(pw):
        found = False
        for char in special_chars:
            if pw.find(char) > -1:
                found = True
        return found

    while not registered:
        print("***Register Password****")
        register_password = input("Enter password: ")

        if caps_found(register_password):
            if special_found(register_password):
                if number_found(register_password):
                    if len(register_password) > 7:
                        registered = True
                        print("Your password has been registered")
                        break
                    else:
                        print("Password must be at least 8 characters long")
                else:
                    print("Password must contain a number")
            else:
                print("Password must contain a special character ('!', '@', '#', '$')")
        else:
            print("Password must contain an uppercase letter")

    # Login check


logged_in = False
failed_attempts = 0
max_attempts = 5

while not logged_in:
    if failed_attempts < max_attempts:
        print("***Login****")
        log_in_pin = input("Enter pin: ")
        if register_password == log_in_pin:
            print("Login successful")
            logged_in = True
        else:
            failed_attempts = failed_attempts + 1
            print("False PIN")
    else:
        print("You have tried to log in too many times")
        break
