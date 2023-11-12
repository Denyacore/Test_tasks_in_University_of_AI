import re

text = '''
Иван, Группа: A123, Средний балл: 4.75
Петр, Группа: B456, Средний балл: 3.92
Елена, Группа: A123, Средний балл: 4.89
Анна, Группа: C789, Средний балл: 4.12
Михаил, Группа: B456, Средний балл: 5.01
Алиса, Группа: A123, Средний балл: 4.98
'''.strip()

with open('data.txt', 'w') as file:
    file.write(text)

with open('data.txt', 'r') as file:
    data = file.read()

students_names_list = re.findall(r'(\w+), Группа:', data)
groups = re.findall(r'Группа: (\w+),', data)
points = re.findall(r'Средний балл: (\d.\d\d)', data)

students = [{'Имя': student_name, 'Группа': group, 'Средний балл': point}
            for student_name, group, point
            in zip(students_names_list, groups, points)]

for student in students:
    print(f"\nИмя: {student['Имя']},\n"
          f"Группа: {student['Группа']},\n"
          f"Средний балл: {student['Средний балл']}")
