import json


class PostDAO:

    def __init__(self, posts, comments):
        self.posts = posts
        self.comments = comments

    def load_data(self):
        with open(self.posts, encoding='utf-8') as file:
            posts = json.loads(file.read())
        with open(self.comments, encoding='utf-8') as file:
            comments = json.loads(file.read())
        return posts, comments

    def get_all_posts(self):
        posts = self.load_data()[0]
        return posts

    def get_all_comments(self):
        comments = self.load_data()[1]
        return comments

    def get_correct_comments_counter(self, lenght_comments):
        str_value = int(str(lenght_comments)[-1])
        if str_value in [2, 3, 4]:
            return 'комментария'
        elif lenght_comments == 11:
            return 'комментариев'
        elif str_value == 1:
            return 'комментарий'
        else:
            return 'комментариев'

    def watching_count(self, post_id):
        with open(self.posts, encoding='utf-8') as file:
            posts = json.loads(file.read())
        with open(self.posts, "w", encoding='utf-8') as file:
            for i in posts:
                if post_id == i['pk']:
                    i["views_count"] += 1
            json.dump(posts, file, ensure_ascii=False, indent=2)