students_path = 'students.txt'


def read_students():
    with open(students_path, 'r') as f:
        return [line.strip('\n').split() for line in f.readlines()]


def write_students(students: list):
    with open('students.txt', 'w') as f:
        for student in students:
            f.write(' '.join(student) + '\n')


def add_student(surname: str, name: str):
    students = read_students()
    students.append([surname, name])
    students.sort()
    write_students(students)


def find_student(surname: str, name=None):
    students = read_students()
    found_students = [student for student in students if student[0] == surname]
    if name is None:
        if len(found_students) == 0:
            return 'Нет студентов с данной фамиилей'
        else:
            return '\n'.join(map(lambda x: ' '.join(x), found_students))
    found_students = [
        student for student in found_students if student[1] == name]
    if len(found_students) == 0:
        return 'Данного студента нет в группе'
    else:
        return 'Данный студент состоит в группе'


def delete_student(surname: str, name=None):
    students = read_students()
    found_students = [student for student in students if student[0] == surname]
    if name is None:
        if len(found_students) == 0:
            return 'Нет студентов с данной фамиилей'
        print('\n'.join(map(lambda x: ' '.join(x), found_students)))
        name = input('Введите имя студента:\n')
    found_students = [
        student for student in found_students if student[1] == name]
    if len(found_students) == 0:
        return 'Данного студента нет в групппе'
    students.remove(found_students[0])
    write_students(students)


def edit_student(surname: str, name: str, new_surname=None, new_name=None):
    msg = delete_student(surname, name)
    if msg is not None:
        print(msg)
        return
    if new_surname is None:
        new_surname = surname
    if new_name is None:
        new_name = name
    add_student(new_surname, new_name)
