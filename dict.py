# Dictionary = {"key" : "value"}

student = {
    "Name": "Ajjima",
    "Age": 31,
    "City": "Bangkok",
    "Pet": ["Dog", "Cat"]
}

print(student)
print(student["Name"])
print(student["Pet"][0])

print("\n-------------------\n")

# method
student.update({"country" : "Thailand"})
print(student)
print(student.keys())
print(student.values())
print(student.get("Pet")) # ดึง value ของ key ออกมา