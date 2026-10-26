# Requirements

# product_name
# รับราคาต่อชิ้น
# รับจำนวนสินค้า
# คำนวณราคารวม
# แสดงใบเสร็จอย่างง่าย
# เพิ่มส่วนลด และแสดงผลอีกรอบ

product_name = input("Enter product name: ")
product_price = float(input("Enter price of product: "))
product_quantity = float(input("Enter quantity of product: "))


print(f"Product: {product_name}")
print(f"Price: {product_price}")
print(f"Quantity: {product_quantity}")

print("=========RECEIPT==========")
print(f"{product_name} x {product_quantity}")
print(f"Total: {product_price*product_quantity:.2f} THB")
print("===================")

discount = int(input("Enter discount of product: "))
print(f"Discount {discount}")

print("=========RECEIPT==========")
print(f"{product_name} x {product_quantity}")
print(f"Discount {discount}%")
print(f"Total: {product_price*product_quantity*(100-discount)/100:.2f} THB")