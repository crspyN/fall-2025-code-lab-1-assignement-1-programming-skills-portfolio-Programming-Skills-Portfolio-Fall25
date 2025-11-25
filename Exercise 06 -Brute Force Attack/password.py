correct_password = "12345"
attempts_left = 5

while attempts_left > 0:
    user_input = input("Enter password: ")

    if user_input == correct_password:
        print("Access granted. Welcome!")
        break
    else:
        attempts_left -= 1
        if attempts_left > 0:
            print(f"Incorrect password. You have {attempts_left} attempt(s) remaining.")
        else:
            print("Maximum attempts reached. Authorities have been alerted.")
