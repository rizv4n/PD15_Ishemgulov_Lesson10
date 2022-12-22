import json


class FeedDAO:

    def __init__(self, path, bookmarks):
        self.path = path
        self.bookmarks = bookmarks

    def load_data(self):
        with open(self.path, encoding='utf-8') as file:
            posts = json.loads(file.read())
        return posts

    def len_bookmarks(self):
        with open(self.bookmarks, encoding='utf-8') as file:
            bookmarks = json.loads(file.read())
        return len(bookmarks)

    def get_all_posts(self):
        posts = self.load_data()
        return posts
