from flask import Blueprint, render_template
from .dao.user_dao import UserDAO

user_blueprint = Blueprint('user_blueprint', __name__)

user_dao = UserDAO("././data/posts.json")

@user_blueprint.route('/post/<user>')
def user_page(user):
    posts = user_dao.get_user_posts(user)
    return render_template('user-feed.html', posts=posts, user=user)
