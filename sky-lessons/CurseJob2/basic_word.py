
class BasicWord:

    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def __repr__(self):
        return "Класс для работы со словарем со словами"

    def check_word(self, user_word):
        return user_word in self.subwords

    def len_subwords(self):
        return len(self.subwords)
