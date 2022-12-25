from flask import Blueprint, render_template, request
from .dao.search_dao import SearchDAO

search_blueprint = Blueprint('search_blueprint', __name__)
search_dao = SearchDAO("././data/posts.json")

@search_blueprint.route('/search')
def search_page():
    s = request.args['s']
    posts = search_dao.search_posts(s)
    len_list = len(posts)
    return render_template('search.html', posts=posts, len=len_list)
