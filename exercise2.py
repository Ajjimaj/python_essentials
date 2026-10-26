# password check

password = "duo42bkk"
attempts = 0

"""
use for loop
for i in range(3):
    user_password = input("Enter your password: ")
    if user_password == password:
        print("Access Granted")
        break
    else:
        print("Access Denied")
else:
    print("Account Locked")
"""

# use while loop
while attempts < 3:
    user_password = input("Enter your password: ")

    if password == user_password:
        print("Access Granted")
        break
    else:
        attempts += 1
        print("Access Denied")

        if attempts == 3:
            print("Account Locked")