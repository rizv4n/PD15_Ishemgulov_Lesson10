from flask import Blueprint, render_template
from .dao.post_dao import PostDAO

post_blueprint = Blueprint('post_blueprint', __name__)

post_dao = PostDAO("././data/posts.json", "././data/comments.json")

@post_blueprint.route('/post/<int:postid>')
def page_post(postid):
    post_dao.watching_count(postid)
    post = post_dao.get_all_posts()[postid - 1]
    all_comments = post_dao.get_all_comments()
    self_comments = []
    for i in all_comments:
        if i['post_id'] == postid:
            self_comments.append(i)
    comm_count = f'{len(self_comments)} {post_dao.get_correct_comments_counter(len(self_comments))}'
    return render_template('post.html', post=post, comments=self_comments, comm_count=comm_count)
