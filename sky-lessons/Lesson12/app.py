from flask import Flask, request, render_template

from functions import get_post_by_word, load_posts
from loader.loader import loader_blueprint, uploads_blueprint
from main.main import main_blueprint

import logging


app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)
app.register_blueprint(uploads_blueprint)


@app.route("/search")
def search_page():
    s = request.args['s']
    if s == [' '] or ['']:
        posts = [i for i in load_posts()]
    else:
        posts = get_post_by_word(s)
    logging.info('Поиск выполнен')
    return render_template('post_list.html', posts=posts)


# @app.route("/uploads/<path:path>")
# def static_dir(path):
#     return send_from_directory("uploads", path)


app.run()
