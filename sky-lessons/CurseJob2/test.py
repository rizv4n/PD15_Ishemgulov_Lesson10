import requests

text = requests.get('https://api.npoint.io/2125f1e51921a9e84eb8')

print(text.text)