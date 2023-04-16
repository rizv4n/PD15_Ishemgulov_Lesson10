import json
import random
import requests
from basic_word import BasicWord

def load_file():
    """
    Функция для чтения файла
    """
    text_file = requests.get('https://api.npoint.io/2125f1e51921a9e84eb8')
    text_convert = json.loads(text_file.text)
    return text_convert

def load_random_word():
    """
    Функция для выбора рандомного слова из списка
    """
    numb = list(range(0, len(load_file())))
    random.shuffle(numb)
    basic_word = BasicWord(load_file()[numb[0]]['word'], load_file()[numb[0]]['subwords'])
    return basic_word

def load_results(results):
    if results == 1:
        return f'Игра завершена! Вы угадали {results} слово'
    elif results in [2, 3, 4]:
        return f'Игра завершена! Вы угадали {results} слова'
    else:
        return f'Игра завершена! Вы угадали {results} слов'
