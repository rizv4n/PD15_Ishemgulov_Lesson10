from flask import Blueprint, render_template, request
import json

loader_blueprint = Blueprint('loader', __name__)
uploads_blueprint = Blueprint('uploads', __name__)

def json_uploads(element):
    with open("./posts.json", 'r+', encoding='utf-8') as file:
        file_convert = json.loads(file.read())
        file_convert.append(element)
        file.seek(0)
        json.dump(file_convert, file, ensure_ascii=False, indent=2)

@loader_blueprint.route('/post')
def page_post_form():
    return render_template('post_form.html')


@uploads_blueprint.route('/post', methods=["POST"])
def page_post_upload():
    picture = request.files.get("picture")
    post_content = request.form['content']
    filename = picture.filename
    format = filename.split(".")[-1]
    if not post_content:
        return render_template('post_is_empty.html')
    elif format not in ['jpg', 'jpeg', 'png']:
        return render_template('post_img_error.html')
    else:
        try:
            json_uploads({'pic': f'../uploads/images/{filename}', 'content': f'{post_content}'})
            picture.save(f"./uploads/images/{filename}")
            return render_template('post_uploaded.html', content=post_content, img=f'./uploads/images/{filename}')
        except:
            return "Ошибка загрузки"
