import random

students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
students.sort()
classes = ['Математика', 'Русский язык', 'Информатика']
students_marks = {}

for student in students:
    students_marks[student] = {}
    for class_ in classes:
        marks = [random.randint(1, 5) for i in range(3)]
        students_marks[student][class_] = marks
for student in students:
    print(f'''{student}
    {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценку ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Добавить ученика
        5. Удалить ученика
        6. Добавить предмет
        7. Удалить предмет
        8. Редактировать оценку ученика по предмету
        9. Удалить оценку ученика по предмету
        10. Вывести все оценки для определенного ученика
        11. Вывести средний балл по каждому предмету для определенного ученика
        12. Редактировать имя ученика
        13. Редактировать название предмета
        14. Вывести средний балл по опредленному предмету для всех учеников
        15. Вывести список учеников
        16. Вывести список предметов
        17. Вывести список отстающих учеников по одному предмету
        18. Вывести список успевающих учеников по одному предмету
        19. Выход из программы
        ''')
while True:
    command = input('Введите команду: ')

    if command == '1':
        print('1. Добавить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        mark = int(input('Введите оценку: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета.')

    elif command == '2':
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        for student in students:
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum // marks_count}')
            print()

    elif command == '3':
        print('3. Вывести все оценки по всем ученикам')
        for student in students:
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()

    elif command == '4':
        print('4. Добавить ученика')
        new_student = input('Введите имя нового ученика: ')
        if new_student not in students:
            students.append(new_student)
            students.sort()
            students_marks[new_student] = {}
            for class_ in classes:
                students_marks[new_student][class_] = []
            print(f'Ученик {new_student} добавлен.')
        else:
            print(f'Ошибка: Такой ученик уже есть.')

    elif command == '5':
        print('5. Удалить ученика')
        student = input('Введите имя ученика для удаления: ')
        if student in students:
            students.remove(student)
            del students_marks[student]
            print('Ученик удален.')
        else:
            print('Ошибка: Такого ученика нет.')

    elif command == '6':
        print('6. Добавить предмет')
        new_class_ = input('Введите название нового предмета: ')
        if new_class_ not in classes:
            classes.append(new_class_)
            for student in students:
                students_marks[student][new_class_] = []
            print(f'Предмет {new_class_} добавлен.')
        else:
            print('Ошибка: Такой предмет уже есть.')

    elif command == '7':
        print('7. Удалить предмет')
        class_ = input('Введите название предмета для удаления: ')
        if class_ in classes:
            classes.remove(class_)
            for student in students:
                del students_marks[student][class_]
            print('Предмет удален.')
        else:
            print('Ошибка: Такого предмета нет.')

    elif command == '8':
        print('8. Редактировать оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        if student in students_marks and class_ in students_marks[student]:
            print(f"Оценки: {students_marks[student][class_]}")
            index = int(input('Введите номер оценки для редактирования (с 0): '))
            if 0 <= index < len(students_marks[student][class_]):
                new_mark = int(input('Введите новую оценку: '))
                students_marks[student][class_][index] = new_mark
                print('Оценка изменена.')
            else:
                print('Ошибка: Неверный номер оценки.')
        else:
            print('Ошибка: Неверный ученик или предмет.')

    elif command == '9':
        print('9. Удалить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        if student in students_marks and class_ in students_marks[student]:
            print(f"Оценки: {students_marks[student][class_]}")
            index = int(input('Введите номер оценки для удаления (с 0): '))
            if 0 <= index < len(students_marks[student][class_]):
                del students_marks[student][class_][index]
                print('Оценка удалена.')
            else:
                print('Ошибка: Неверный номер оценки.')
        else:
            print('Ошибка: Неверный ученик или предмет.')

    elif command == '10':
        print('10. Вывести все оценки для определенного ученика')
        student = input('Введите имя ученика: ')
        if student in students_marks:
            print(f"Оценки для {student}:")
            for class_, marks in students_marks[student].items():
                print(f"  {class_}: {marks}")
        else:
            print('Ошибка: Такого ученика нет.')

    elif command == '11':
        print('11. Вывести средний балл по каждому предмету для определенного ученика')
        student = input('Введите имя ученика: ')
        if student in students_marks:
            print(f"Средний балл по предметам для {student}:")
            for class_ in classes:
                if class_ in students_marks[student] and students_marks[student][class_]:
                    print(f"  {class_}: {sum(students_marks[student][class_]) / len(students_marks[student][class_])}")
                else:
                    print(f"  {class_}: Нет оценок")
        else:
            print('Ошибка: Такого ученика нет.')

    elif command == '12':
        print('12. Редактировать имя ученика')
        old_student = input('Введите имя ученика для редактирования: ')
        if old_student in students:
            new_student = input('Введите новое имя ученика: ')
            students[students.index(old_student)] = new_student  # Replace in students list
            students.sort()  # Keep sorted
            students_marks[new_student] = students_marks.pop(old_student)  # Rename key
            print('Имя ученика изменено.')
        else:
            print('Ошибка: Такого ученика нет.')

    elif command == '13':
        print('13. Редактировать название предмета')
        old_class = input('Введите название предмета для редактирования: ')
        if old_class in classes:
            new_class = input('Введите новое название предмета: ')
            classes[classes.index(old_class)] = new_class
            for student in students:
                students_marks[student][new_class] = students_marks[student].pop(old_class)
            print('Название предмета изменено.')
        else:
            print('Ошибка: Такого предмета нет.')

    elif command == '14':
        print('14. Вывести средний балл по опредленному предмету для всех учеников')
        class_ = input('Введите название предмета: ')
        if class_ in classes:
            print(f"Средний балл по предмету {class_} для всех учеников:")
            for student in students:
                if class_ in students_marks[student] and students_marks[student][class_]:
                    average = sum(students_marks[student][class_]) / len(students_marks[student][class_])
                    print(f"  {student}: {average}")
                else:
                    print(f"  {student}: Нет оценок")
        else:
            print('Ошибка: Такого предмета нет.')

    elif command == '15':
        print('15. Вывести список учеников')
        print("Список учеников:")
        for student in students:
            print(student)

    elif command == '16':
        print('16. Вывести список предметов')
        print("Список предметов:")
        for class_ in classes:
            print(class_)

    elif command == '17':
        print('17. Вывести список отстающих учеников по одному предмету')
        class_ = get_class_ = input("Введите предмет, по которому нужно вывести список отстающих: ")
        if not class_:
            continue
        print(f"Список отстающих по предмету {class_} (средний балл < 3):")
        for student in students:
            if class_ in students_marks[student]:
                marks = students_marks[student][class_]
                if marks:
                    average = sum(marks) / len(marks)
                    if average < 3:
                        print(f" {student}: {average:.2f}")
                else:
                    print(f" {student}: Нет оценок")
            else:
                print(f" {student}: Нет данных по этому предмету")

    elif command == '18':
        print('18. Вывести список успевающих учеников по одному предмету')
        class_ = get_class_ = input("Введите предмет, по которому нужно вывести список успевающих: ")
        if not class_:
            continue
        print(f"Список успевающих по предмету {class_} (средний балл >= 4):")
        for student in students:
            if class_ in students_marks[student]:
                marks = students_marks[student][class_]
                if marks:
                    average = sum(marks) / len(marks)
                    if average >= 4:
                        print(f" {student}: {average:.2f}")
                else:
                    print(f" {student}: Нет оценок")
            else:
                print(f" {student}: Нет данных по этому предмету")

    elif command == '19':  # Выход
        print('19. Выход из программы')
        break

    else:
        print('Неверная команда.')
