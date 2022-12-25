from pathlib import Path
import json

path = Path('tests','json_for_test.json')

with open(path, encoding='utf-8') as file:
    f = json.loads(file.read())
    print(f)