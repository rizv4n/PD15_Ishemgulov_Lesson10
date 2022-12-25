import json


class SearchDAO:

    def __init__(self, path):
        self.path = path

    def load_data(self):
        with open(self.path, encoding='utf-8') as file:
            posts = json.loads(file.read())
        return posts

    def search_posts(self, word):
        posts = self.load_data()
        what_matches = []
        count = 0
        for i in posts:
            if count < 10:
                if word.lower() in i['content'].lower():
                    what_matches.append(i)
                    count += 1
            else:
                break
        return what_matches
