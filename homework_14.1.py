import os
from collections import defaultdict

# Создаем файл, если его нет
if not os.path.exists("students.txt"):
    try:
        with open("students.txt", "w") as f:
            f.write("")
    except Exception as e:
        print(f"Ошибка при создании файла: {e}")

# Записываем информацию о студентах
students_info = [
    ("Student1", "Group1", 85),
    ("Student2", "Group1", 90),
    ("Student3", "Group2", 88),
    ("Student4", "Group2", 87),
    ("Student5", "Group3", 88),
]

try:
    with open("students.txt", "w") as f:
        for student in students_info:
            f.write(f"{student[0]}, {student[1]}, {student[2]}\\n")
except Exception as e:
    print(f"Ошибка при записи в файл: {e}")

# Читаем информацию из файла
try:
    with open("students.txt", "r") as f:
        lines = f.readlines()
except Exception as e:
    print(f"Ошибка при чтении из файла: {e}")

# Считаем статистику
total_students = len(lines)
group_students = defaultdict(int)
group_scores = defaultdict(list)

for line in lines:
    student, group, score = line.strip().split(", ")
    group_students[group] += 1
    group_scores[group].append(int(score))

# Печатаем статистику и записываем ее в файл
try:
    with open("students.txt", "a") as f:
        f.write(f"\\nTotal students: {total_students}\\n")
        for group in group_students:
            avg_score = sum(group_scores[group]) / group_students[group]
            f.write(f"Group {group}: {group_students[group]} students, average score: {avg_score}\\n")
except Exception as e:
    print(f"Ошибка при записи в файл: {e}")