"""HOMEWORK 14.1"""

with open("students.txt", "w+", encoding="utf-8") as file:
    student_list = file.write("Biba, 1, 8\n"
                              "Boba, 1, 7\n"
                              "Boka, 2, 3\n"
                              "Joka, 2, 6\n"
                              "Pepa, 2, 10\n"
                              "Repa, 3, 5\n")


with open("students.txt", "r", encoding="utf-8") as file:
    data = file.readlines()
    group_1 = group_2 = group_3 = 0
    exam_1 = exam_2 = exam_3 = 0
    try:
        for line in data:
            student, group, exam = line.split(", ")
            if group == "1":
                group_1 += 1
                exam_1 += int(exam)
            if group == "2":
                group_2 += 1
                exam_2 += int(exam)
            if group == "3":
                group_3 += 1
                exam_3 += int(exam)
            students_total = group_1 + group_2 + group_3

        exam_1 = exam_1 / group_1
        exam_2 = exam_2 / group_2
        exam_3 = exam_3 / group_3

    except ZeroDivisionError:
        print("There are no students in one or more groups!")

    except ValueError:
        print("Wrong input data or format: please ensure that "
              "input data follows next pattern: {str}, {int}, {int}")

#
with open("students.txt", "a", encoding="utf-8") as file:
    file.write(f"\n"
               f"Total students: {students_total}\n"
               f"First group exam results: {round(exam_1, 1)}\n"
               f"Second group exam results: {round(exam_2, 1)}\n"
               f"Third group exam results: {round(exam_3, 1)}")
