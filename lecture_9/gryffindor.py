students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

gryffindor = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindor):  # prints in the sorted order
    print(gryffindor)
