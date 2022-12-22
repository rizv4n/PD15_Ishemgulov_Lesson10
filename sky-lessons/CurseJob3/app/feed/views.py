from flask import Blueprint, render_template
from .dao.feed_dao import FeedDAO

feed_blueprint = Blueprint('feed_blueprint', __name__)
feed_dao = FeedDAO("././data/posts.json", "././data/bookmarks.json")


@feed_blueprint.route('/')
def page_feed():
    posts = feed_dao.get_all_posts()
    len_bookmarks = feed_dao.len_bookmarks()
    return render_template('index.html', posts=posts, len=len_bookmarks)
