import json

def load_students():
    """
    Функция для загрузки списка студентов
    """
    with open("students_list.txt") as file:
        file_convert = json.loads(file.read())
        return file_convert

def load_professions():
    """
    Функция для загрузки списка профессий
    """
    with open("professions_list.txt") as file:
        file_convert = json.loads(file.read())
        return file_convert

def get_student_by_pk(pk):
    """
    Функция для поиска студента по его номеру
    """
    for i in load_students():
        if pk == i['pk']:
            return i['full_name'], i['skills']

def get_profession_be_title(title):
    """
    Функция для поиска скилов для профессии
    """
    for i in load_professions():
        if title.title() == i['title']:
            return i['skills']

def check_fitness(student, profession):
    """
    Функция для определения соотвествия скилов к профессии
    """
    total_list = {}
    student_skills = set(get_student_by_pk(student)[1])
    profession_skills = set(get_profession_be_title(profession))
    total_list['has'] = list(student_skills.intersection(profession_skills))
    total_list['lacks'] = list(student_skills.difference(profession_skills))
    total_list['fit_percent'] = round(len(total_list['has'])/(len(total_list['has'])+len(total_list['lacks']))*100)
    return total_list
