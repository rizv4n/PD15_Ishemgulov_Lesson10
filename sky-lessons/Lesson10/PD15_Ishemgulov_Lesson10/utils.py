import json

def load_candidates():
    """
    Функция для загрузки данных из файла
    """
    with open("candidates.json", encoding='utf-8') as file:
        file_convert = json.loads(file.read())
        return file_convert

def get_all():
    """
    Функция возвращающая всех кандидатов
    """
    all_names = []
    for i in load_candidates():
        all_names.append("\n".join(["  " + i['name'],"  " + str(i['pk']),"  " + i['skills']]))
    return "\n\n".join(all_names)

def get_by_pk(pk):
    """
    Функция возвращающая кандидата по pk
    """
    for i in load_candidates():
        if pk == i['pk']:
            candidate_profile = "\n".join(["  " + i['name'], "  " + str(i['pk']), "  " + i['skills']])
            url = '<img src="({i["picture"]})">'
            return candidate_profile, url

def get_by_skill(skill_name):
    """
    Функция возвращающая кандидата по скиллу
    """
    who_matches = []
    for i in load_candidates():
        skills_list = i['skills'].replace(" ", "").split(',')
        skills_list_lower = [j.lower() for j in skills_list]
        if skill_name.lower() in skills_list_lower:
            who_matches.append("\n".join(["  " + i['name'],"  " + str(i['pk']),"  " + i['skills']]))
    return "\n\n".join(who_matches)