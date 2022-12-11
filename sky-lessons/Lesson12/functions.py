import json

try:
    def load_posts():
        """
        Функция для загрузки данных из файла
        """
        with open("posts.json", encoding='utf-8') as file:
            file_convert = json.loads(file.read())
            return file_convert
except:
    print("Файл posts.json отсутствует или не хочет превращаться в список")


def del_points(string):
    """
    Функция для удаления точек из текста
    """
    while True:
        if string.endswith('.'):
            string = string[0:len(string) - 1]
        else:
            return string


def del_symbols(string):
    """
    Функция для удаления символов из текста
    """
    dirty_list = [',', '!', '#', '.', ':', '?']
    clean_list = []
    for i in string.split(' '):
        new_list = list(del_points(i))
        for j in new_list:
            if j in dirty_list:
                new_list.remove(j)
        clean_list.append("".join(new_list).lower())
    return clean_list


def get_post_by_word(word):
    """
    Функция возвращающая пост по слову
    """
    what_matches = []
    for i in load_posts():
        post_description = del_symbols(i['content'])
        if word in post_description:
            what_matches.append(i)
    return what_matches
