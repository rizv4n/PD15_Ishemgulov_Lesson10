from flask import Blueprint, render_template, redirect
from .dao.bookmarks_dao import BookmarksDAO

bookmarks_blueprint = Blueprint('bookmarks_blueprint', __name__)
bookmarks_add_blueprint = Blueprint('bookmarks_add_blueprint', __name__)
bookmarks_del_blueprint = Blueprint('bookmarks_del_blueprint', __name__)
bookmarks_dao = BookmarksDAO("././data/posts.json", "././data/bookmarks.json")


@bookmarks_blueprint.route('/bookmarks')
def bookmarks_page():
    bookmarks = bookmarks_dao.load_bookmarks()
    return render_template('bookmarks.html', posts=bookmarks)


@bookmarks_add_blueprint.route('/bookmarks/add/<int:postid>')
def bookmarks_add(postid):
    bookmarks_dao.add_bookmark(postid)
    return redirect('/', code=302)


@bookmarks_del_blueprint.route('/bookmarks/del/<int:postid>')
def bookmarks_del(postid):
    bookmarks_dao.del_bookmark(postid)
    return redirect('/bookmarks', code=302)