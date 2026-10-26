"""
age = int(input("Enter your age: "))

if age >= 18:
    print("You can join this party!")
else:
    print("You cann't join this party bye bye~")

age = int(input("Enter your age: "))
# has_ticket = True
has_ticket = input("Do you have ticket [yes/no]: ")

if age >= 18 and has_ticket == "yes":
    print("You can join this concert!")
else:
    print("You must over 18 and have ticket to join this concert")
"""

## elif: check more than 1 condition / when first if != True
score = int(input("Enter your score: "))

if score >= 80:
    print("You Got A")
elif score >= 70:
    print("You Got B")
elif score >= 60:
    print("You Got C")
elif score >=50:
    print("You Got D")
else:
    print("You Got F. See you next semester")
