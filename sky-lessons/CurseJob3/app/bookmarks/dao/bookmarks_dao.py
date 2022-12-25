import json


class BookmarksDAO:

    def __init__(self, path, bookmarks):
        self.path = path
        self.bookmarks = bookmarks

    def load_data(self):
        with open(self.path, encoding='utf-8') as file:
            posts = json.loads(file.read())
        return posts

    def load_bookmarks(self):
        with open(self.bookmarks, encoding='utf-8') as file:
            bookmarks_numb = json.loads(file.read())
            bookmarks = []
            for i in self.load_data():
                for j in bookmarks_numb:
                    if i['pk'] == j:
                        bookmarks.append(i)
        return bookmarks

    def add_bookmark(self, post_id):
        with open(self.bookmarks, 'r', encoding='utf-8') as file:
            bookmarks = json.loads(file.read())
            for i in bookmarks:
                if post_id == i:
                    return
        with open(self.bookmarks, 'w', encoding='utf-8') as file:
            for i in self.load_data():
                if post_id == i['pk']:
                    bookmarks.append(i['pk'])
            json.dump(bookmarks, file)

    def del_bookmark(self, post_id):
        with open(self.bookmarks, 'r', encoding='utf-8') as file:
            bookmarks = json.loads(file.read())
        with open(self.bookmarks, 'w', encoding='utf-8') as file:
            for i in bookmarks:
                if post_id == i:
                    bookmarks.remove(i)
            json.dump(bookmarks, file)