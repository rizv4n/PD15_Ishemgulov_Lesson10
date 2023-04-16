import random

#Ввод переменных
user_name = input('Введите ваше имя: ')
user_count = 0
user_games = 0
user_fullcount = 0

#Главная программа на угадывание слов
with open("words.txt") as file:
    words_list = [line.rstrip() for line in file]
    for i in range(5):
        word_for_test = random.choice(words_list)
        words_list.remove(word_for_test)
        letter_for_shuffle = [i for i in word_for_test]
        random.shuffle(letter_for_shuffle)
        shuffle_letter = "".join(letter_for_shuffle)
        user_answer = input(f'Угадайте слово {shuffle_letter}\n')
        if user_answer.lower() == word_for_test:
            user_count += 10
            print('Верно! Вы получаете 10 очков.\n')
        else:
            print(f'Неверно! Верный ответ – {word_for_test}.\n')

print(f'{user_name}, вы набрали {user_count} очков')

#Запись истории в отдельный файл
with open("history.txt", "a") as file:
    file.write(f'\n{user_name}:{user_count}')

#Вывод общих результатов в сравнении с топом
with open("history.txt") as file:
    users_list = [line.rstrip() for line in file]
    for i in users_list:
        if user_name in i:
            if int(i.split(":")[1]) > user_fullcount:
                user_fullcount = int(i.split(":")[1])

print(f'Всего игр сыграно: {user_games}\nМаксимальный рекорд: {user_fullcount}')
