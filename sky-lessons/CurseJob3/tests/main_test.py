import pytest

from main import app
keys = ["poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"]


class TestApi:

    def test_app(self):
        response = app.test_client().get('/api/posts')
        assert type(response.json) == list, "Ошибка в формате файла"
        for i in response.json:
            for j in i.keys():
                assert j in keys, "Неверное количество или содержание ключей в файле"

    def test_app_id(self):
        response = app.test_client().get('/api/posts/1')
        assert type(response.json) == dict, "Ошибка в формате файла"
        for i in response.json.keys():
            assert i in keys, "Неверное количество или содержание ключей в файле"
