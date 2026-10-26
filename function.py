# greeting function
def greet(name):
    print(f"Hello, {name}!")

greet("Ajjima")

# calulate function
def calculate_total(price, quantity):
    total = price * quantity
    return total

result = calculate_total(500, 5)
print(f"Total: {result}")

def calculate(a,b):
    total = a + b
    print(total)

calculate(5, 10)

result = calculate(5,10) # ถ้าไม่ได้ใส่ return ใน function ก็จะมีการส่งค่า None คืนกลับมาด้วย
print(result)

def calculate_with_return(a,b):
    total = a + b
    return total

result = calculate_with_return(5,15)
print(result)

# print  : แสดงผลออก console เพื่อดูค่าเท่านั้น ไม่ได้เก็บค่าไว้ใช้ต่อ
# return : ส่งค่าผลลัพธ์กลับออกมาจากฟังก์ชัน เพื่อนำไปเก็บใส่ตัวแปรหรือคำนวณต่อได้
# ถ้าฟังก์ชันไหนไม่มีคำสั่ง return ฟังก์ชันนั้นจะคืนค่าเป็น None เสมอ