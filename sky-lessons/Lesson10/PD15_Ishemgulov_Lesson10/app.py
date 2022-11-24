from utils import get_all, get_by_pk, get_by_skill

from flask import Flask

app = Flask(__name__)

@app.route('/')
def page_index():
    return f'<pre>\n{get_all()}\n</pre>'

@app.route('/candidates/<int:x>')
def page_profile(x):
    return f'<img src="{get_by_pk(x)[1]}">\n\n<pre>\n{get_by_pk(x)[0]}\n</pre>'

@app.route('/skills/<x>')
def page_skills(x):
    return f'<pre>\n{get_by_skill(x)}\n</pre>'

app.run()
