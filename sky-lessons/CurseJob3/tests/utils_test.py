import pytest

from app.feed.dao.feed_dao import FeedDAO


feed_dao_instance = FeedDAO('tests/json_for_test.json', 'tests/json_for_test.json')


def test_for_init():
    feed = feed_dao_instance.load_data()
    assert feed == [{'post_id': 1, 'comment': 'Очень здорово!'}], "Неверная инициализация"
