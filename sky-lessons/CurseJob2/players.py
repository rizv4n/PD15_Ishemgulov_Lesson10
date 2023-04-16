
class Player:

    def __init__(self, username):
        self.username = username
        self.used_words = []

    def __repr__(self):
        return "Класс для работы с данными игрока и их сбора"

    def len_used_words(self):
        return len(self.used_words)

    def add_used_words(self, word):
        self.used_words.append(word)

    def check_word(self, word_for_check):
        return word_for_check in self.used_words