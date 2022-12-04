from flask import Flask

app = Flask(__name__)

@app.route("/")
def page_index():
    return "Главная страничка"

@app.route("/profile/<uid>")
def page_profile(uid=1):
    return f'<h1>Профиль {uid}</h1>'

@app.route('/catalog/items/<itemid>')
def profile(itemid):
    return f'<h1>Страничка товара {itemid}</h1>'

app.run(host='127.0.0.2', port=80)