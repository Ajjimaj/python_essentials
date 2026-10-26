"""shopping_list = []

item_input = input("Enter item: ")

while item_input != "done":
    shopping_list.append(item_input)
    item_input = input("Enter item: ")

print("Shopping list:")
for i, item in enumerate(shopping_list, start=1):
    print(f"{i}. {item}")
"""
"""
enumerate() คือฟังก์ชันที่ใช้ในการวนลูปผ่าน object หรือ iterable อื่น ๆ 
และให้ค่าดัชนี (index) ของแต่ละรายการพร้อมกับค่าของรายการนั้น ๆ ในขณะที่วนลูปอยู่ 
โดยค่าดัชนีจะเริ่มต้นจาก 0 by default แต่สามารถกำหนดค่าเริ่มต้นได้โดยใช้พารามิเตอร์ start
"""

shopping_list = []

while True:
    item_input = input("Enter item (or type 'done' to finish): ")
    if item_input.lower() == "done":
        break
    shopping_list.append(item_input)

print("Shopping list:")
for i in range(len(shopping_list)):
    print(f"{i + 1}. {shopping_list[i]}")