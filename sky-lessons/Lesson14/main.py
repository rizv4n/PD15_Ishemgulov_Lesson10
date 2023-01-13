from flask import Flask

from app.seacrh import get_title_by_word, correct_result_title
from app.year_to_year import get_title_by_year, correct_result_year
from app.rating import get_title_by_rating, correct_result_rating

app = Flask(__name__)

direct = "netflix.db"


@app.route('/movie/<title>')
def search_by_title(title):
    movie = get_title_by_word(title, direct)
    return correct_result_title(movie)


@app.route('/movie/<int:from_year>/to/<int:to_year>')
def search_by_years(from_year, to_year):
    movies = get_title_by_year(from_year, to_year, direct)
    return correct_result_year(movies)


@app.route('/rating/<rating>')
def search_by_rating(rating):
    if rating == 'children':
        rating_list = ('G', '')
        movies = get_title_by_rating(rating_list, direct)
        return correct_result_rating(movies)
    elif rating == 'family ':
        rating_list = ('G', 'PG', 'PG-13')
        movies = get_title_by_rating(rating_list, direct)
        return correct_result_rating(movies)
    elif rating == 'adult':
        rating_list = ('R', 'NC-17')
        movies = get_title_by_rating(rating_list, direct)
        return correct_result_rating(movies)
    else:
        return 'Некорректный выбор рейтинга'


if __name__ == '__main__':
    app.run()
