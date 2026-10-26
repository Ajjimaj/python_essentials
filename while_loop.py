# while loops

i = 1

while i <= 5:
    print("Hello Python", i)
    i += 1 # i = i + 1

# while loop and input
while True:
    password = input("Enter your password: ")

    if password == "1234":
        print("Login Successful")
        break

    print("Wrong Password!, Please try again")