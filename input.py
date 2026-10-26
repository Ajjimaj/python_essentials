# รับค่าจาก user
"""
name = input("Enter your name: ")
print("Welcome", name)

# input รับค่าเป็น string

age = int(input("Enter your age: "))
print(type(age))

print("Your age is ", age)
print(type(age))
"""

price = float(input("Enter Price: "))
quantity = float(input("Enter Quantity: "))

total = price * quantity
print(f"Total price is : {total:.2f}") # .2f == ทศนิยม 2 ตำแหน่ง
