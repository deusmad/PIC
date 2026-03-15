groupmates = [
    {
        "name": u"Василий",
        "group": "912-2",
        "age": 19,
        "marks": [4, 3, 5, 5, 4]
    },
    {
        "name": u"Анна",
        "group": "912-1",
        "age": 18,
        "marks": [3, 2, 3, 4, 3]
    },
    {
        "name": u"Георгий",
        "group": "912-2",
        "age": 19,
        "marks": [3, 5, 4, 3, 5]
    },
    {
        "name": u"Валентина",
        "group": "912-1",
        "age": 18,
        "marks": [5, 5, 5, 4, 5]
    }
]


def print_students(students):
    """Print all stud."""
    print(u"Имя студента".ljust(15),
          u"Группа".ljust(8),
          u"Возраст".ljust(8),
          u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15),
              student["group"].ljust(8),
              str(student["age"]).ljust(8),
              str(student["marks"]).ljust(20))
    print("\n")


def stud_filter_average_score(students: list[dict], score: int) -> list:
    """Stud filter avg."""
    passed_stud = []
    for student in students:
        marks: list[int] = student.get('marks', [])
        if sum(marks) / len(marks) < score:
            continue
        passed_stud.append(student)

    return passed_stud


passed_stud = stud_filter_average_score(groupmates, 4)

print_students(passed_stud)
print_students(groupmates)
