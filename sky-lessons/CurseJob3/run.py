from flask import Flask, jsonify
import json

from app.feed.views import feed_blueprint
from app.post.views import post_blueprint
from app.search.views import search_blueprint
from app.user.views import user_blueprint
from app.bookmarks.views import bookmarks_blueprint, bookmarks_add_blueprint, bookmarks_del_blueprint

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(feed_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(bookmarks_blueprint)
app.register_blueprint(bookmarks_add_blueprint)
app.register_blueprint(bookmarks_del_blueprint)


@app.route('/api/posts')
def api_posts():
    with open('data/posts.json', encoding='utf-8') as file:
        file_api = json.loads(file.read())
        return jsonify(file_api)


@app.route('/api/posts/<int:post_id>')
def api_post(post_id):
    with open('data/posts.json', encoding='utf-8') as file:
        file_api = json.loads(file.read())
        for i in file_api:
            if post_id == i['pk']:
                return jsonify(i)


@app.errorhandler(404)
def page_not_found(e):
    return f'Ошибка {e}'


@app.errorhandler(500)
def page_not_found(e):
    return f'Ошибка {e}'


if __name__ == "__main__":
    app.run()
