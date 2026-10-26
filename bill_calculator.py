# Simple Bill Calculator

# price of product
# quantity of product
# total price
# show result

product_name = input("What you want to buy?: ")
product_price = float(input("Enter the price of product: "))
product_quantity = float(input("Qunatity: "))

total = product_price * product_quantity

print("===== RECEIPT =====")
print(f"Product Name: {product_name}")
print(f"Product Price: {product_price}")
print(f"Product Qunatity: {product_quantity}")
print(f"total price: {total:.2f} THB")