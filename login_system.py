
correct_username = 'admin'
correct_password = '1234'

attempts = 3

# enter the pass n username
while attempts > 0:
    username = input("Enter the username: ")
    password = input("Enter the password: ")

    if username == correct_username and password == correct_password:
        print("Login Successfully !")
        break
    else:
# attempts fails!
        attempts -= 1
        print(f"Incorrect Credentials. Left Attempts {attempts}")

        if attempts == 0:
            print("Attempts Over")
