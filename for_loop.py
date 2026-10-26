# for loop

for num in range(0, 7):
    print(num)

for i in range(5):
    print("Hello Python")

for i in range(1, 11):
    if i == 5:
        break
    print("Hello Python", i)

# continue ข้ามรอบนี้ไปต่อรอบหน้า
for i in range(1, 6):
    if i == 2: # ถ้า i == 2 ให้ข้าม
        continue # และรันต่อไป
    print(i)

for i in range(3):
    print(i, end=' ')