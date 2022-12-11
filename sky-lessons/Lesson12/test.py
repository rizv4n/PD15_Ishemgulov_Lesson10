from functions import json_uploads, load_posts
import json

with open("posts.json", 'r+', encoding='utf-8') as file:
    file_convert = json.loads(file.read())
    file_convert.append({'pic':'111', 'content':'2222'})
    file.seek(0)
    json.dump(file_convert, file, ensure_ascii=False, indent=2)
print(file_convert)