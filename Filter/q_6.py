students = [
    {"name": "Denis Helio", "age": 17, "grade": 97},
    {"name": "Hania Mehtap", "age": 16, "grade": 92},
    {"name": "Kiran Stan", "age": 17, "grade": 90},
    {"name": "Velvet Mirko", "age": 16, "grade": 94},
    {"name": "Delores Aeneas", "age": 17, "grade": 100},
]
print(list(filter(lambda x: x["grade"] > 95, students)))
