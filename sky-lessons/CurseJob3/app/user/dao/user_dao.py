import json


class UserDAO:

    def __init__(self, posts):
        self.posts = posts

    def load_data(self):
        with open(self.posts, encoding='utf-8') as file:
            posts = json.loads(file.read())
        return posts

    def get_user_posts(self, user):
        posts = self.load_data()
        what_matches = []
        for i in posts:
            if user in i['poster_name']:
                what_matches.append(i)
        return what_matches
