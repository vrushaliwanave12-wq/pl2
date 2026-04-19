student = {"name": "Rishabh", "division": 15, "age": 18}
print(student)

print(student["name"])

student["division"] = 15
student["city"] = "Pune"
print(student)

del student["age"]
print(student)

more_info = {"sport": "Soccer", "hobby": "Art"}
student.update(more_info)
print(student)