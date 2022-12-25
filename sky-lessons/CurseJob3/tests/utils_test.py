import pytest

from app.bookmarks.dao.bookmarks_dao import BookmarksDAO
from app.feed.dao.feed_dao import FeedDAO
from app.post.dao.post_dao import PostDAO
from app.search.dao.search_dao import SearchDAO
from app.user.dao.user_dao import UserDAO

file_restore = 'data/json_for_test.json'
file2_restore = 'data/json_for_test2.json'
file_content = [{'pk': 1, 'poster_name': 'kerry', 'content': 'Очень здорово!'}]
file2_content = [1]
comments_counting = [
    {'count': 3, 'text': 'комментария'},
    {'count': 21, 'text': 'комментарий'},
    {'count': 30, 'text': 'комментариев'}
]

feed_dao_instance = FeedDAO(file_restore, file2_restore)
bookmarks_dao_instance = BookmarksDAO(file_restore, file2_restore)
post_dao_instance = PostDAO(file_restore, file_restore)
search_dao_instance = SearchDAO(file_restore)
user_dao_instance = UserDAO(file_restore)


class TestApp:

    def test_for_bookmarks(self):
        posts = bookmarks_dao_instance.load_data()
        bookmarks = bookmarks_dao_instance.load_bookmarks()
        assert posts == file_content, "Неверная инициализация постов"
        assert bookmarks == file_content, "Неверная инициализация файла bookmarks"

    def test_for_feed(self):
        feed = feed_dao_instance.load_data()
        len_list = feed_dao_instance.len_bookmarks()
        posts = feed_dao_instance.get_all_posts()
        assert feed == file_content, "Неверная инициализация ленты"
        assert len_list == 1, "Неверный подсчет количества bookmarks"
        assert posts == file_content, "Неверная инициализация постов"

    def test_for_post(self):
        posts = post_dao_instance.load_data()[0]
        comments = post_dao_instance.load_data()[1]
        posts_getting = post_dao_instance.get_all_posts()
        comments_getting = post_dao_instance.get_all_comments()
        assert posts == file_content, "Неверная инициализация постов"
        assert comments == file_content, "Неверная инициализация комментариев"
        assert posts_getting == file_content, "Неверная инициализация постов"
        assert comments_getting == file_content, "Неверная инициализация комментариев"
        for i in comments_counting:
            content = post_dao_instance.get_correct_comments_counter(i['count'])
            assert content == i['text'], "Орфографическая ошибка при подсчете комментариев"

    def test_for_search(self):
        posts = search_dao_instance.load_data()
        search = search_dao_instance.search_posts('Очень')
        assert posts == file_content, "Неверная инициализация загрузки постов для поиска"
        assert search == file_content, "Ошибка при поиске постов"

    def test_for_user(self):
        posts = user_dao_instance.load_data()
        user = user_dao_instance.get_user_posts('kerry')
        assert posts == file_content, "Неверная инициализация постов"
        assert user == file_content, "Ошибка при поиске постов пользователя"
