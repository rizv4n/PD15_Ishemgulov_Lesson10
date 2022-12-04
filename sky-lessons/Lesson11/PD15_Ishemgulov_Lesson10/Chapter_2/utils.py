import json

def load_candidates():
    """
    Функция для загрузки данных из файла
    """
    with open("candidates.json", encoding='utf-8') as file:
        file_convert = json.loads(file.read())
        return file_convert

def load_candidates_from_json():
    """
    Функция возвращающая всех кандидатов
    """
    all_names = [[i['name'],i['id']] for i in load_candidates()]
    return all_names

def get_candidates(candidate_id):
    """
    Функция возвращающая кандидата по id
    """
    for i in load_candidates():
        if candidate_id == i['id']:
            return i['name'], str(i['id']), i['skills'], i["picture"]

def get_candidates_by_name(candidate_name):
    """
    Функция возвращающая кандидата по имени
    """
    who_matches = []
    for i in load_candidates():
        name_list = i['name'].split(' ')
        name_list_lower = [j.lower() for j in name_list]
        if candidate_name.lower() in name_list_lower:
            who_matches.append([i['name'], str(i['id'])])
    return who_matches

def get_candidates_by_skill(skill_name):
    """
    Функция возвращающая кандидата по скиллу
    """
    who_matches = []
    for i in load_candidates():
        skills_list = i['skills'].replace(" ", "").split(',')
        skills_list_lower = [j.lower() for j in skills_list]
        if skill_name.lower() in skills_list_lower:
            who_matches.append([i['name'], str(i['id'])])
    return who_matches
