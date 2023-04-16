from players import Player
from utils import load_random_word, load_results

#Знакомство с игроком
username = str(input('Введите ваше имя: '))

player = Player(username)
print(f'Здравствуй, {player.username}!')

playing_word = load_random_word()
print(f'Составьте {playing_word.len_subwords()} слов из слова {playing_word.word}'
      f'\nСлова должны быть не короче 3 букв\nЧтобы закончить игру, угадайте все слова или напишите "stop"'
      f'\nПоехали, ваше первое слово?')

#Запуск цикла игры по угадыванию слов
counter = 0
while counter < playing_word.len_subwords():
    user_word = input().lower()
    if user_word == 'stop':
        break
    elif len(user_word) < 3:
        print('Слишком короткое слово')
        continue
    elif user_word not in playing_word.subwords:
        print('Неверно')
        continue
    elif player.check_word(user_word):
        print('Уже использовано')
    else:
        player.add_used_words(user_word)
        counter += 1
        print('Правильно!')

#Вывод результатов игры
print(load_results(player.len_used_words()))
