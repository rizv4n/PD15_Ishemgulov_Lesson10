from functions import load_posts

for i in load_posts():
    print(i['content'])