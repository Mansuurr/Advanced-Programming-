import json
import os
base_dir = os.path.dirname(__file__)
input_path = os.path.join(base_dir, "students.json")
output_path = os.path.join(base_dir, "students_with_average.json")
with open(input_path, "r", encoding="utf-8") as file:
    students = json.load(file)
for student in students:
    grades = student["grades"]
    student["average_grade"] = sum(grades) / len(grades)
with open(output_path, "w", encoding="utf-8") as file:
    json.dump(students, file, indent=2)
