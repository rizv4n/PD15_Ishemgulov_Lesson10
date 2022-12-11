from flask import Blueprint, render_template, request
import json

loader_blueprint = Blueprint('loader', __name__)
uploads_blueprint = Blueprint('uploads', __name__)

try:
    def json_uploads(element):
        with open("./posts.json", 'r+', encoding='utf-8') as file:
            file_convert = json.loads(file.read())
            file_convert.append(element)
            file.seek(0)
            json.dump(file_convert, file, ensure_ascii=False, indent=2)
except:
    print("Файл posts.json отсутствует или не хочет превращаться в список")


@loader_blueprint.route('/post')
def page_post_form():
    return render_template('post_form.html')


try:
    @uploads_blueprint.route('/post', methods=["POST"])
    def page_post_upload():
        picture = request.files.get("picture")
        post_content = request.form['content']
        filename = picture.filename
        json_uploads({'pic': f'../uploads/images/{filename}', 'content': f'{post_content}'})
        picture.save(f"./uploads/images/{filename}")
        return render_template('post_uploaded.html', content=post_content, img=f'./uploads/images/{filename}')
except:
    @uploads_blueprint.route('/post', methods=["POST"])
    def page_post_upload():
        return "Ошибка загрузки"
