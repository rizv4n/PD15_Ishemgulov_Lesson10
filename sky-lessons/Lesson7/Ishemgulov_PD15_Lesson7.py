import sys
from utils import get_student_by_pk, get_profession_be_title, check_fitness

# Получение номера студента и проверка наличия его в списках
student_number = int(input('Введите номер студента'))
check_student = get_student_by_pk(student_number)
if check_student is None:
    print("У нас нет такого студента")
    sys.exit()

# Вывод информации по студенту
print(f'Студент {check_student[0]}\nЗнает {", ".join(check_student[1])}')

# Получение профессии и проверка наличия его в списках
profession = input(f'Выберите специальность для оценки студента {check_student[0]}')
skills_for_profession = get_profession_be_title(profession)
if skills_for_profession is None:
    print("У нас нет такой специальности")
    sys.exit()
output = check_fitness(student_number, profession)

# Вывод результатов программы
print(f'Пригодность {output["fit_percent"]}%\n{check_student[0]} знает {", ".join(output["has"])}\n{check_student[0]} не знает {", ".join(output["lacks"])}')