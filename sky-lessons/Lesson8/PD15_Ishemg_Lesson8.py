import json
import random

#Создаем класс и инициализируем его по всем необходимым параметрам и добавляем необходимые функции
class Question:
    def __init__(self, quest_text, quest_diff, quest_ans, user_ans = None, is_asked = False):
        self.quest_text = quest_text
        self.quest_diff = int(quest_diff)
        self.quest_ans = quest_ans
        self.is_asked = is_asked
        self.user_ans = user_ans
        self.points = self.quest_diff * 10

    def get_points(self):
        return self.points

    def is_correct(self):
        return self.quest_ans == self.user_ans

    def build_question(self):
        return f"\nВопрос: {self.quest_text}\nСложность {self.quest_diff}/5"

    def build_feedback(self, is_correct_ = True):
        if is_correct_:
            return f"Ответ верный, получено {self.get_points()} баллов"
        else:
            return f"Ответ неверный, верный ответ - {self.quest_ans}"

def load_file():
    """Функция для чтения файла с вопросами"""
    with open("questions_for_test.txt") as file:
        file_convert = json.loads(file.read())
    return file_convert

def get_questions():
    """Функция лоя получение списка вопросов"""
    questions = []
    for i in load_file():
        questions.append(Question(i['q'], i['d'], i['a']))
    return questions

def get_scores(questions_list):
    """Функция для подсчета очков"""
    correct_answers = []
    score = 0
    for i in questions_list:
        if i.is_correct():
            correct_answers.append(i.user_ans)
            score += i.get_points()
    return f"\nВот и всё!\nОтвечено {len(correct_answers)} вопроса из 10\nНабрано баллов: {score}"

questions_with_answers = []
len_quest = [i for i in range(len(get_questions()))]

get_scores(get_questions())

#Работа программы в виде цикла for
for i in range(len(len_quest)):
    random.shuffle(len_quest)
    print(get_questions()[len_quest[0]].build_question())
    user_answer = str(input('\nВведите ответ: '))
    numb = load_file()[len_quest[0]]
    questions_with_answers.append(Question(numb['q'], numb['d'], numb['a'], user_answer, True))
    print(questions_with_answers[i].build_feedback(questions_with_answers[i].is_correct()))
    len_quest.pop(0)

print(get_scores(questions_with_answers))
